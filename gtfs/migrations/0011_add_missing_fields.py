# Generated by Django 3.1.7 on 2021-04-07 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gtfs", "0010_add_rider_category"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="route",
            name="unique_feed_gtfs_route",
        ),
        migrations.AddField(
            model_name="agency",
            name="logo_url",
            field=models.URLField(blank=True, verbose_name="logo URL"),
        ),
        migrations.AddField(
            model_name="route",
            name="sort_order",
            field=models.PositiveSmallIntegerField(
                blank=True, null=True, verbose_name="sort order"
            ),
        ),
        migrations.AddField(
            model_name="stop",
            name="tts_name",
            field=models.CharField(
                blank=True,
                help_text="readable version of the name",
                max_length=255,
                verbose_name="TTS name",
            ),
        ),
        migrations.AddField(
            model_name="stop",
            name="wheelchair_boarding",
            field=models.PositiveSmallIntegerField(
                choices=[(0, "Unknown"), (1, "Possible"), (2, "Not possible")],
                default=0,
                verbose_name="wheelchair boarding",
            ),
        ),
        migrations.AddField(
            model_name="stoptime",
            name="timepoint",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (0, "Times are considered approximate"),
                    (1, "Times are considered exact"),
                ],
                default=1,
                verbose_name="timepoint",
            ),
        ),
        migrations.AddField(
            model_name="trip",
            name="bikes_allowed",
            field=models.PositiveSmallIntegerField(
                choices=[(0, "Unknown"), (1, "Allowed"), (2, "Not allowed")],
                default=0,
                verbose_name="bikes allowed",
            ),
        ),
        migrations.AddField(
            model_name="trip",
            name="capacity_sales",
            field=models.PositiveSmallIntegerField(
                choices=[(0, "Disabled"), (1, "Enabled"), (2, "Required")],
                default=0,
                verbose_name="capacity sales",
            ),
        ),
        migrations.AddField(
            model_name="trip",
            name="wheelchair_accessible",
            field=models.PositiveSmallIntegerField(
                choices=[(0, "Unknown"), (1, "Accessible"), (2, "Not accessible")],
                default=0,
                verbose_name="wheelchair accessible",
            ),
        ),
    ]
