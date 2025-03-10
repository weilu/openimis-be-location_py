# Generated by Django 3.2.16 on 2023-08-16 09:34

from django.db import migrations, models
from location.models import HealthFacility

class Migration(migrations.Migration):

    dependencies = [
        ('location', '0015_set_managed_to_true'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthfacility',
            name='contract_end_date',
            field=models.DateTimeField(blank=True, db_column='ContractEndDate', null=True),
        ),
        migrations.AddField(
            model_name='healthfacility',
            name='contract_start_date',
            field=models.DateTimeField(blank=True, db_column='ContractStartDate', null=True),
        )
        ]

        

