from django.apps import AppConfig
from django.db.models.signals import post_save, post_migrate

class UsermanagerConfig(AppConfig):
    name = 'usermanager'

    def ready(self):
        from .signals import add_permissions, define_groups
        post_migrate.connect(define_groups, sender=self)
        post_save.connect(add_permissions, sender=self)

