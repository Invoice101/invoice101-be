from django.conf import settings
from django.db.models import CharField, EmailField, ForeignKey, CASCADE, PROTECT, ImageField, BooleanField
from django.db.models.signals import post_delete
from django.dispatch import receiver
from model_utils.models import UUIDModel

from invoice_101.contact.utils import get_contact_image_path
from invoice_101.core.models import State
from invoice_101.utils.common_utils import GSTValidator, PinCodeValidator
from .constants import CONTACT_TYPE_CHOICES


class Contact(UUIDModel):
    owner = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    name = CharField(max_length=255)
    email = EmailField()

    company = CharField(max_length=255, blank=True, null=True)
    mobile_no = CharField(max_length=15, blank=True, null=True)

    image = ImageField(upload_to=get_contact_image_path, blank=True, null=True)
    is_customer = BooleanField(default=True)
    is_supplier = BooleanField(default=True)

    billing_address_line_1 = CharField(max_length=512, blank=True, null=True)
    billing_address_line_2 = CharField(max_length=512, blank=True, null=True)
    billing_city = CharField(max_length=100, blank=True, null=True)
    billing_state = ForeignKey(State, on_delete=PROTECT, related_name='customer_billing_state')
    billing_pin_code = CharField(max_length=6, validators=[PinCodeValidator], blank=True, null=True)

    shipping_address_line_1 = CharField(max_length=512, blank=True, null=True)
    shipping_address_line_2 = CharField(max_length=512, blank=True, null=True)
    shipping_city = CharField(max_length=100, blank=True, null=True)
    shipping_state = ForeignKey(State, on_delete=PROTECT, blank=True, null=True, related_name='customer_shipping_state')
    shipping_pin_code = CharField(max_length=6, validators=[PinCodeValidator], blank=True, null=True)

    gstin = CharField(max_length=15, validators=[GSTValidator], blank=True, null=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return f'{self.name} - {self.owner}'


@receiver(post_delete, sender=Contact)
def contact_delete(sender, instance, **kwargs):
    instance.image.delete(False)
