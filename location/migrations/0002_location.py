# Generated by Django 2.1.9 on 2019-07-26 06:07

import core.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("location", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.AutoField(
                        db_column="LocationId", primary_key=True, serialize=False
                    ),
                ),
                (
                    "legacy_id",
                    models.IntegerField(blank=True, db_column="LegacyId", null=True),
                ),
                (
                    "code",
                    models.CharField(
                        blank=True, db_column="LocationCode", max_length=8, null=True
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, db_column="LocationName", max_length=50, null=True
                    ),
                ),
                (
                    "parent",
                    models.IntegerField(
                        blank=True, db_column="ParentLocationId", null=True
                    ),
                ),
                ("type", models.CharField(db_column="LocationType", max_length=1)),
                (
                    "validity_from",
                    core.fields.DateTimeField(
                        blank=True, db_column="ValidityFrom", null=True
                    ),
                ),
                (
                    "validity_to",
                    core.fields.DateTimeField(
                        blank=True, db_column="ValidityTo", null=True
                    ),
                ),
                (
                    "male_population",
                    models.IntegerField(
                        blank=True, db_column="MalePopulation", null=True
                    ),
                ),
                (
                    "female_population",
                    models.IntegerField(
                        blank=True, db_column="FemalePopulation", null=True
                    ),
                ),
                (
                    "other_population",
                    models.IntegerField(
                        blank=True, db_column="OtherPopulation", null=True
                    ),
                ),
                (
                    "families",
                    models.IntegerField(blank=True, db_column="Families", null=True),
                ),
                (
                    "audit_user_id",
                    models.IntegerField(blank=True, db_column="AuditUserId", null=True),
                ),
            ],
            options={
                "db_table": "tblLocations",
                "managed": False,
            },
        ),
    ]
