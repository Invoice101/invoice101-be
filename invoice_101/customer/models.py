from django.conf import settings
from django.core.validators import RegexValidator
from django.db.models import CharField, EmailField, ForeignKey, CASCADE, PROTECT
from model_utils.models import UUIDModel

from invoice_101.core.models import State
from invoice_101.utils.common_utils import GSTValidator, PinCodeValidator


class Customer(UUIDModel):
    owner = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    name = CharField(max_length=255)
    email = EmailField()

    company = CharField(max_length=255, blank=True, null=True)
    mobile_no = CharField(max_length=15, blank=True, null=True)

    gstin = CharField(max_length=15, validators=[GSTValidator], blank=True, null=True)

    address_line_1 = CharField(max_length=512, blank=True, null=True)
    address_line_2 = CharField(max_length=512, blank=True, null=True)
    city = CharField(max_length=100, blank=True, null=True)
    state = ForeignKey(State, on_delete=PROTECT)
    pin_code = CharField(max_length=6, validators=[PinCodeValidator], blank=True, null=True)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return f'{self.name} - {self.owner}'
