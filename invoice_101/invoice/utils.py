from datetime import timedelta
from uuid import uuid4

from django.utils import timezone


def get_invoice_file_path(instance, filename):
    ext = 'pdf'
    filename = "user/%s/invoices/%s.%s" % (instance.user.id, uuid4(), ext)
    return filename


def get_default_valid_till():
    return timezone.now() + timedelta(days=7)
