# Generated by Django 3.1.7 on 2021-04-19 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("gtfs", "0016_add_helper_m2m_fields"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="fareridercategory",
            name="api_id",
        ),
    ]
