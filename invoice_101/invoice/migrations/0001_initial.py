# Generated by Django 3.0.5 on 2020-05-01 07:25

from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import invoice_101.invoice.utils
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contact', '0002_auto_20200425_1405'),
        ('product', '0001_initial'),
        ('core', '0002_gstslab_uom'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('DRAFT', 'Draft'), ('SENT', 'Sent'), ('RECEIVED', 'Payment Received'), ('CANCELLED', 'Cancelled'), ('DUE', 'Overdue')], default='DRAFT', max_length=32)),
                ('number', models.CharField(blank=True, max_length=32, null=True, verbose_name='Invoice Number')),
                ('document', models.FileField(blank=True, null=True, upload_to=invoice_101.invoice.utils.get_invoice_file_path)),
                ('valid_till', models.DateTimeField(default=invoice_101.invoice.utils.get_default_valid_till)),
                ('subtotal', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('tax', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('rounding', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=2)),
                ('discount', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('amount', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('billing_address_line_1', models.CharField(blank=True, max_length=512, null=True)),
                ('billing_address_line_2', models.CharField(blank=True, max_length=512, null=True)),
                ('billing_city', models.CharField(blank=True, max_length=100, null=True)),
                ('billing_pin_code', models.CharField(blank=True, max_length=6, null=True, validators=[django.core.validators.RegexValidator('^\\d{6}$', 'Invalid PinCode.')])),
                ('shipping_address_line_1', models.CharField(blank=True, max_length=512, null=True)),
                ('shipping_address_line_2', models.CharField(blank=True, max_length=512, null=True)),
                ('shipping_city', models.CharField(blank=True, max_length=100, null=True)),
                ('shipping_pin_code', models.CharField(blank=True, max_length=6, null=True, validators=[django.core.validators.RegexValidator('^\\d{6}$', 'Invalid PinCode.')])),
                ('tnc', models.TextField(blank=True, max_length=1024, null=True, verbose_name='Terms and Conditions')),
                ('service_required_on', models.DateTimeField(blank=True, null=True)),
                ('additional_details', models.CharField(blank=True, max_length=2000, null=True)),
                ('billing_state', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='invoice_billing_state', to='core.State')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='contact.Contact')),
                ('shipping_state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='invoice_shipping_state', to='core.State')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Invoice',
                'verbose_name_plural': 'Invoices',
            },
        ),
        migrations.CreateModel(
            name='InvoiceLine',
            fields=[
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('hsn_sac', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=2000, null=True)),
                ('quantity', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('unit_price', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=12)),
                ('gross_unit_price', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=12)),
                ('discount', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=12)),
                ('tax', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=8)),
                ('tax_amount', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=12)),
                ('amount', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='invoice.Invoice')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
            options={
                'verbose_name': 'Invoice Entry',
                'verbose_name_plural': 'Invoice Entries',
            },
        ),
    ]
