from django.db import models
from uuid import uuid4
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    uuid = models.UUIDField(
        _("Unique identifier"),
        primary_key=True,
        default=uuid4,
        unique=True,
        editable=False
    )
    is_active = models.BooleanField(
        _("Is active"),
        default=True
    )
    created = models.DateTimeField(
        _("Created"),
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        _("Updated"),
        auto_now=True
    )

    class Meta:
        abstract = True


class Airplane(BaseModel):
    FUEL_CONSUMPTION_MULTIPLIER = 0.80
    LITRE_CAPACITY_MULTIPLIER = 200
    PASSENGER_FUEL_CONSUMPTION_MULTIPLIER = 0.002

    type_id = models.IntegerField(
        _("Type ID"),
        default=1
    )
    passenger_assumption = models.IntegerField(
        _("Passenger Assumption"),
        default=0
    )

    class Meta:
        verbose_name = _("Airplane")
        verbose_name_plural = _("Airplanes")
