from decimal import Decimal

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db.models import ForeignKey, CharField, FileField, DateTimeField, DecimalField, PositiveIntegerField, \
    TextField, PROTECT, CASCADE, Model
from model_utils.models import UUIDModel, TimeStampedModel

from invoice_101.contact.models import Contact
from .constants import INVOICE_STATUS_CHOICES
from .utils import get_invoice_file_path, get_default_valid_till
from ..core.models import State
from ..product.models import Product
from ..utils.common_utils import PinCodeValidator


class Invoice(UUIDModel):
    subject = CharField(max_length=200)
    user = ForeignKey(settings.AUTH_USER_MODEL, related_name='invoices', on_delete=CASCADE)
    contact = ForeignKey(Contact, related_name='invoices', on_delete=CASCADE)
    status = CharField(max_length=32, choices=INVOICE_STATUS_CHOICES, default='DRAFT')

    number = CharField(max_length=32, verbose_name='Invoice Number', blank=True, null=True)
    document = FileField(upload_to=get_invoice_file_path, blank=True, null=True)
    valid_till = DateTimeField(default=get_default_valid_till)

    subtotal = DecimalField(max_digits=15, decimal_places=2, default=Decimal(0.00))
    tax = DecimalField(max_digits=15, decimal_places=2, default=Decimal(0.00))
    rounding = DecimalField(max_digits=2, decimal_places=2, default=Decimal(0.00))
    discount = DecimalField(max_digits=15, decimal_places=2, default=Decimal(0.00))
    amount = DecimalField(max_digits=15, decimal_places=2, default=Decimal(0.00))

    # Billing Address
    billing_address_line_1 = CharField(max_length=512, blank=True, null=True)
    billing_address_line_2 = CharField(max_length=512, blank=True, null=True)
    billing_city = CharField(max_length=100, blank=True, null=True)
    billing_state = ForeignKey(State, on_delete=PROTECT, related_name='invoice_billing_state')
    billing_pin_code = CharField(max_length=6, validators=[PinCodeValidator], blank=True, null=True)

    # Shipping Address
    shipping_address_line_1 = CharField(max_length=512, blank=True, null=True)
    shipping_address_line_2 = CharField(max_length=512, blank=True, null=True)
    shipping_city = CharField(max_length=100, blank=True, null=True)
    shipping_state = ForeignKey(State, on_delete=PROTECT, blank=True, null=True, related_name='invoice_shipping_state')
    shipping_pin_code = CharField(max_length=6, validators=[PinCodeValidator], blank=True, null=True)

    tnc = TextField(max_length=1024, blank=True, null=True, verbose_name='Terms and Conditions')

    # Service Fields
    service_required_on = DateTimeField(blank=True, null=True)
    additional_details = CharField(blank=True, null=True, max_length=2000)

    class Meta:
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'

    def __str__(self):
        return f'{self.number} - {self.contact}'


class InvoiceLine(UUIDModel):
    name = CharField(max_length=100)
    hsn_sac = CharField(max_length=50, blank=True, null=True)
    description = CharField(max_length=2000, blank=True, null=True)
    product = ForeignKey(Product, blank=True, null=True, on_delete=CASCADE)

    quantity = PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    unit_price = DecimalField(max_digits=12, decimal_places=2, default=Decimal(0.00))
    gross_unit_price = DecimalField(max_digits=12, decimal_places=2, default=Decimal(0.00))

    discount = DecimalField(max_digits=12, decimal_places=2, default=Decimal(0.00))
    tax = DecimalField(max_digits=8, decimal_places=2, default=Decimal(0.00))
    tax_amount = DecimalField(max_digits=12, decimal_places=2, default=Decimal(0.00))

    amount = DecimalField(max_digits=15, decimal_places=2, default=Decimal(0.00))
    invoice = ForeignKey(Invoice, related_name='items', on_delete=CASCADE)

    class Meta:
        verbose_name = 'Invoice Entry'
        verbose_name_plural = 'Invoice Entries'

    def __str__(self):
        return '%s' % self.name
