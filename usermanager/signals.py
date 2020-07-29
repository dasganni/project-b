from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver

from .models import User


def create_or_edit_group(name, permissions):
    group, created_group = Group.objects.get_or_create(name=name)
    if len(permissions) > 0:
        [group.permissions.add(permission) for permission in permissions]


# after database migrate, so in the beginning, create the needed usergroups
# and assign rights
@receiver(post_migrate, sender=User)
def define_groups(sender, **kwargs):
    # standard usergroup
    permissions = [
        Permission.objects.get(codename="add_game"),
    ]
    create_or_edit_group("default_usergroup", permissions)
    # other groups defined here


# when user is created, assign him to the default_usergroup
@receiver(post_save, sender=User)
def add_permissions(sender, instance, created, **kwargs):
    if created:
        if not instance.username == "AnonymousUser":
            my_group = Group.objects.get(name="default_usergroup")
            my_group.user_set.add(instance)