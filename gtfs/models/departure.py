from uuid import uuid5

from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _

from .base import API_ID_NAMESPACE
from .trip import Trip


class Departure(models.Model):
    api_id = models.UUIDField(verbose_name=_("API ID"), unique=True)
    trip = models.ForeignKey(
        Trip,
        verbose_name=_("trip"),
        on_delete=models.CASCADE,
    )
    date = models.DateField(verbose_name=_("date"))

    class Meta:
        verbose_name = _("departure")
        verbose_name_plural = _("departures")
        default_related_name = "departures"
        constraints = [
            models.UniqueConstraint(
                fields=["trip", "date"],
                name="unique_trip_instance_date",
            )
        ]

    def __str__(self):
        return f"{self.date} {self.trip}"

    def populate_api_id(self):
        self.api_id = uuid5(
            API_ID_NAMESPACE,
            f"{self.__class__.__name__}:{self.trip.feed_id}:{self.trip.source_id}:{self.date}",
        )

    def save(self, *args, **kwargs):
        if not self.api_id:
            self.populate_api_id()
        super().save(*args, **kwargs)
