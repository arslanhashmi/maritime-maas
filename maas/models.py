from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class MaasOperator(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=64)
    identifier = models.CharField(
        verbose_name=_("identifier"),
        max_length=64,
        unique=True,
        help_text=_(
            "Value is sent in an API call to a ticketing system. Identifies the MaaS "
            "operator in a ticketing system."
        ),
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="maas_operator",
        verbose_name=_("user"),
    )
    transport_service_providers = models.ManyToManyField(
        "TransportServiceProvider", related_name="maas_operators", through="Permission"
    )

    class Meta:
        verbose_name = _("maas operator")
        verbose_name_plural = _("maas operators")

    def __str__(self):
        return self.name


class TransportServiceProvider(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=64)
    ticketing_system = models.ForeignKey(
        "maas.TicketingSystem",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("ticketing system"),
    )

    class Meta:
        verbose_name = _("transport service provider")
        verbose_name_plural = _("transport service provider")
        default_related_name = "transport_service_providers"

    def __str__(self):
        return self.name


class Permission(models.Model):
    maas_operator = models.ForeignKey(MaasOperator, on_delete=models.CASCADE)
    transport_service_provider = models.ForeignKey(
        TransportServiceProvider, on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _("permission")
        verbose_name_plural = _("permissions")
        default_related_name = "permissions"

    def __str__(self):
        return f"{self.maas_operator.name} - {self.transport_service_provider.name}"


class TicketingSystem(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=64)
    api_key = models.CharField(
        verbose_name=_("API key"),
        max_length=255,
        blank=True,
        help_text=_("API key that will be used for accessing the API"),
    )
    bookings_api_url = models.URLField(verbose_name=_("API bookings endpoint URL"))
    availability_api_url = models.URLField(
        verbose_name=_("API availability endpoint URL"), blank=True
    )

    class Meta:
        verbose_name = _("ticketing system")
        verbose_name_plural = _("ticketing systems")

    def __str__(self):
        return self.name
