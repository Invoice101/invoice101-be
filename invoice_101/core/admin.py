from django.contrib import admin

# Register your models here.
from .models import State

admin.site.site_header = "Invoice 101 Administration"

admin.site.register(State)
