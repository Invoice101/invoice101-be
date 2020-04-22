from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db.models import CharField, ForeignKey, PROTECT
from django.utils.translation import ugettext_lazy as _

from invoice_101.core.models import State
from invoice_101.utils.common_utils import GSTValidator, PinCodeValidator


class User(AbstractUser):
    name = CharField(_("Name of User"), max_length=255)
    mobile_no = CharField(_("Mobile Number"), max_length=15, validators=[
        RegexValidator(regex=r'^[0-9]{10,15}$', message='Invalid Mobile Number')
    ], blank=True, null=True, unique=True)

    # Address
    company = CharField(max_length=512, blank=True, null=True)
    address_line_1 = CharField(max_length=512, blank=True, null=True)
    address_line_2 = CharField(max_length=512, blank=True, null=True)
    city = CharField(max_length=100, blank=True, null=True)
    state = ForeignKey(State, on_delete=PROTECT, blank=True, null=True)
    pin_code = CharField(max_length=6, validators=[PinCodeValidator], blank=True, null=True)
    gst = CharField(max_length=15, validators=[GSTValidator], blank=True, null=True)
