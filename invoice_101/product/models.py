from decimal import Decimal

from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import ForeignKey, CharField, DecimalField, PROTECT, CASCADE
from model_utils.models import UUIDModel

from invoice_101.core.models import GSTSlab, UOM


class Product(UUIDModel):
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    name = CharField(max_length=500)
    description = CharField(max_length=2000, blank=True, null=True)
    hsn_sac = CharField(max_length=30, blank=True, null=True)
    tax_percentage = DecimalField(default=Decimal(0.0), max_digits=5, decimal_places=2,
                                  validators=[MinValueValidator(0), MaxValueValidator(100)])

    price = DecimalField(default=Decimal(0.0), max_digits=12, decimal_places=2)
    uom = ForeignKey(UOM, on_delete=PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
