#Python Image as base
FROM python:3.8-slim

#Install Python Requirements
COPY requirements.txt /tmp/

# Install build deps, then run `pip install`, then remove unneeded build deps all in a single step. Also install some packages which will not be removed after.
RUN set -ex \
    && BUILD_DEPS=" \
    python3-dev \
    gcc \
    " \
    && apt-get update && apt-get install -y --no-install-recommends $BUILD_DEPS \
    && apt-get install -y --no-install-recommends libpq-dev libnss-wrapper gettext curl \
    && pip install --no-cache-dir -r /tmp/requirements.txt \
    \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $BUILD_DEPS \
    && rm -rf /var/lib/apt/lists/*

# Create a group and user to run the app
RUN useradd -m -d /pnp-manager/ -s /bin/bash -c "Default Docker User for the Container" -u 1000 -g 0 pnp-manager

# Copy the application code to the container
COPY --chown=1000:0 . /pnp-manager/
RUN chmod -R g+w /pnp-manager/docker/

WORKDIR /pnp-manager/

# UWSGI Settings and default needed environments for the server itself
ENV UWSGI_WSGI_FILE=django_server/wsgi.py \
    UWSGI_HTTP=:8000 UWSGI_MASTER=1 \
    UWSGI_HTTP_AUTO_CHUNKED=1 \
    UWSGI_HTTP_KEEPALIVE=1 \
    UWSGI_LAZY_APPS=1 \
    UWSGI_WSGI_ENV_BEHAVIOR=holy \
    UWSGI_WORKERS=2 \
    UWSGI_THREADS=4 \
    UWSGI_STATIC_MAP="/static/=/pnp-manager/static/" \
    UWSGI_STATIC_EXPIRES_URI="/static/.*\.[a-f0-9]{12,}\.(css|js|png|jpg|jpeg|gif|ico|woff|ttf|otf|svg|scss|map|txt) 315360000" \
    \
    DJANGO_SERVER_ENVIRONMENT="prod" \
    DJANGO_DB_ENGINE=django.db.backends.postgresql \
    DJANGO_DB_NAME=pnp-manager DJANGO_DB_USER=pnp-manager \
    DJANGO_DB_PASSWORD=pnp-manager DJANGO_DB_HOST=database \
    DJANGO_DB_PORT=5432 \
    LD_PRELOAD=libnss_wrapper.so \
    NSS_WRAPPER_PASSWD=/pnp-manager/docker/passwd \
    NSS_WRAPPER_GROUP=/etc/group \
    DJANGO_SUPERUSER_ADMIN=admin \
    DJANGO_SUPERUSER_PASSWORD=admin \
    DJANGO_SUPERUSER_EMAIL=admin@localhost.com

# Change to a non-root user
USER 1000

# the server will listen on this port
EXPOSE 8000

#Start the container and execute the following:
ENTRYPOINT ["/pnp-manager/docker/docker-entrypoint.sh"]