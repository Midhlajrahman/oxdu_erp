# Generated by Django 4.2.7 on 2025-02-26 10:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="HistoricalBranch",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(blank=True, db_index=True, editable=False),
                ),
                ("updated", models.DateTimeField(blank=True, editable=False)),
                ("name", models.CharField(max_length=100)),
                ("address", models.TextField(blank=True, null=True)),
                ("city", models.CharField(blank=True, max_length=100, null=True)),
                ("state", models.CharField(blank=True, max_length=100, null=True)),
                ("country", models.CharField(blank=True, max_length=100, null=True)),
                ("postal_code", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "contact_number",
                    models.CharField(blank=True, max_length=15, null=True),
                ),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                (
                    "manager_name",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("opening_date", models.DateField(blank=True, null=True)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical branch",
                "verbose_name_plural": "historical Branches",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="Branch",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100)),
                ("address", models.TextField(blank=True, null=True)),
                ("city", models.CharField(blank=True, max_length=100, null=True)),
                ("state", models.CharField(blank=True, max_length=100, null=True)),
                ("country", models.CharField(blank=True, max_length=100, null=True)),
                ("postal_code", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "contact_number",
                    models.CharField(blank=True, max_length=15, null=True),
                ),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                (
                    "manager_name",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("opening_date", models.DateField(blank=True, null=True)),
                (
                    "creator",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="%(app_label)s_%(class)s_creator",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Branches",
                "ordering": ["-created"],
                "abstract": False,
            },
        ),
    ]
