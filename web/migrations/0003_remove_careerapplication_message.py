# Generated by Django 5.0.1 on 2024-03-13 13:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0002_delete_eventregistration_remove_event_description_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="careerapplication",
            name="message",
        ),
    ]
