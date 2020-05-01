from decimal import Decimal

from django.db import models
# Create your models here.
from django.db.models import CharField, DecimalField, BooleanField
from django_extensions.db.models import TimeStampedModel


class State(models.Model):
    name = models.CharField(max_length=100, unique=True)
    short_name = models.CharField(max_length=10, unique=True)
    code = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name = 'State'
        verbose_name_plural = 'States'

    def __str__(self):
        return f'{self.name}'


class GSTSlab(TimeStampedModel):
    name = CharField(max_length=64, unique=True)
    tax = DecimalField(max_digits=5, decimal_places=2, default=Decimal(0.0))
    cess = DecimalField(max_digits=5, decimal_places=2, default=Decimal(0.0))
    total = DecimalField(max_digits=5, decimal_places=2, default=Decimal(0.0))
    active = BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'GST Slab'
        verbose_name_plural = 'GST Slabs'


class UOM(TimeStampedModel):
    short_name = CharField(max_length=10, unique=True, primary_key=True)
    name = CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Unit of measure'
        verbose_name_plural = 'Units of measure'
