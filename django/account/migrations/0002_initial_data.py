from django.db import migrations
from django.core.management.sql import emit_post_migrate_signal
from django.contrib.auth.models import Group

def insert_groups(apps, schema_editor):
    """
    Inserts the default user Groups
    """

    for name in ['Admin', 'Moderator']:
        Group.objects.get_or_create(name=name)


def add_group_permissions(apps,schema_editor):
    """
    Add relevant permissions to specified group

    As permissions are set following initial migration,
    the few bits of extra lines are needed to ensure that permissions have been created
    """

    # Ensure permissions and content types have been created.
    db_alias = schema_editor.connection.alias
    emit_post_migrate_signal(2, False, db_alias)

    # Recommended way to get Group and Permission (vs importing)
    Group = apps.get_model("auth", "Group")
    Permission = apps.get_model('auth', "Permission")

    # List of permissions (view, add, change, delete) for each model within each app for each group
    group_permissions_list = [

        # Admin permissions
        {
            "group_name": "Admin",
            "apps": [
                {
                    "app_name": "account",
                    "models": [
                        {
                            "model_name": "user",
                            "permissions": ['view', 'add', 'change', 'delete']
                        },
                    ]
                },
                {
                    "app_name": "visions",
                    "models": [
                        {
                            "model_name": "vision",
                            "permissions": ['view', 'add', 'change', 'delete']
                        },
                        {
                            "model_name": "response",
                            "permissions": ['view', 'add', 'change', 'delete']
                        },
                    ]
                },
                {
                    "app_name": "inspirations",
                    "models": [
                        {
                            "model_name": "inspiration",
                            "permissions": ['view', 'add', 'change', 'delete']
                        },
                    ]
                }
            ],
        },

        # Moderator permissions
        {
            "group_name": "Moderator",
            "apps": [
                {
                    "app_name": "visions",
                    "models": [
                        {
                            "model_name": "vision",
                            "permissions": ['view', 'add', 'change']
                        },
                        {
                            "model_name": "response",
                            "permissions": ['view', 'add', 'change']
                        },
                    ]
                },
                {
                    "app_name": "inspirations",
                    "models": [
                        {
                            "model_name": "inspiration",
                            "permissions": ['view', 'add', 'change']
                        },
                    ]
                }
            ]
        }

    ]

    # Loop through group > app > model > permission to define all of the permissions set in group_permissions_list
    for group in group_permissions_list:
        g = Group.objects.get(name=group['group_name'])
        for app in group['apps']:
            a = app['app_name']
            for model in app['models']:
                for permission in model['permissions']:
                    g.permissions.add(Permission.objects.get(codename=f"{permission}_{model['model_name']}", content_type__app_label=a))


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial')
    ]

    operations = [
        migrations.RunPython(insert_groups),
        migrations.RunPython(add_group_permissions)
    ]
