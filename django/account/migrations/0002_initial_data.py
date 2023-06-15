from django.db import migrations
from account import models
from django.contrib.auth.models import Group

def insert_groups(apps, schema_editor):
    """
    Inserts the default user Groups
    """

    for name in [
        'Admin',
        'Moderator',
        'Member',
    ]:
        Group.objects.get_or_create(name=name)


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial')
    ]

    operations = [
        migrations.RunPython(insert_groups),
    ]
