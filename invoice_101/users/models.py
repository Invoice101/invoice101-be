from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db.models import CharField
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    name = CharField(_("Name of User"), max_length=255)
    mobile_no = CharField(_("Mobile Number"), max_length=15, validators=[
        RegexValidator(regex=r'^[0-9]{10,15}$', message='Invalid Mobile Number')
    ], blank=True, null=True, unique=True)
