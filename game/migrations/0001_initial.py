# Generated by Django 3.0.3 on 2020-02-20 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=60, verbose_name='Titel')),
                ('title_slug', models.SlugField(default='', editable=False, max_length=60)),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('access_restricted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'game',
                'verbose_name_plural': 'games',
                'ordering': ['-creation_date'],
                'permissions': (('view_game', 'Can view game'),),
                'default_permissions': ('add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='GameGroupObjectPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GameUserObjectPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Game')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Permission')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]