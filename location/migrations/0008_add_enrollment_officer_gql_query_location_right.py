# Generated by Django 3.0.14 on 2021-11-03 10:46

from django.db import migrations
from core.utils import insert_role_right_for_system, remove_role_right_for_system

IMIS_EO_ROLE_IS_SYSTEM = 1

def forwards_func(apps, schema_editor):
    RoleRight = apps.get_model('core', 'RoleRight')
    Role = apps.get_model('core', 'Role')
    # Add enrollment officer right to read location data
    insert_role_right_for_system(IMIS_EO_ROLE_IS_SYSTEM, 121901, apps)

def reverse_func(apps, schema_editor):
    RoleRight = apps.get_model('core', 'RoleRight')
    Role = apps.get_model('core', 'Role')
    # Same data as in forward function
    remove_role_right_for_system(IMIS_EO_ROLE_IS_SYSTEM, 121901, apps)

class Migration(migrations.Migration):

    dependencies = [
        ("location", "0007_auto_20211103_1046"),
        ('core', '0015_missing_roles')

    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
