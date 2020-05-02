from django.core.management import BaseCommand

from invoice_101.core.models import UOM

uom_list = [
    {'name': 'Bag', 'short_name': 'BAG'},
    {'name': 'Bale', 'short_name': 'BAL'},
    {'name': 'Bundles', 'short_name': 'BDL'},
    {'name': 'Buckles', 'short_name': 'BKL'},
    {'name': 'Billions of units', 'short_name': 'BOU'},
    {'name': 'Box', 'short_name': 'BOX'},
    {'name': 'Bottles', 'short_name': 'BTL'},
    {'name': 'Bunches', 'short_name': 'BUN'},
    {'name': 'Cans', 'short_name': 'CAN'},
    {'name': 'Cubic Meter', 'short_name': 'CBM'},
    {'name': 'Centimeter', 'short_name': 'CMS'},
    {'name': 'Cartons', 'short_name': 'CTN'},
    {'name': 'Dozen', 'short_name': 'DZN'},
    {'name': 'Drum', 'short_name': 'DRM'},
    {'name': 'Great Gross', 'short_name': 'GGR'},
    {'name': 'Grams', 'short_name': 'GMS'},
    {'name': 'Gross', 'short_name': 'GRS'},
    {'name': 'Gross Yards', 'short_name': 'GYD'},
    {'name': 'Kilograms', 'short_name': 'KGS'},
    {'name': 'Kiloliter', 'short_name': 'KLR'},
    {'name': 'Kilometer', 'short_name': 'KME'},
    {'name': 'Milliliter', 'short_name': 'MLT'},
    {'name': 'Meters', 'short_name': 'MTR'},
    {'name': 'Metric Ton', 'short_name': 'MTS'},
    {'name': 'Numbers', 'short_name': 'NOS'},
    {'name': 'Packs', 'short_name': 'PAC'},
    {'name': 'Pieces', 'short_name': 'PCS'},
    {'name': 'Pairs', 'short_name': 'PRS'},
    {'name': 'Quintal', 'short_name': 'QTL'},
    {'name': 'Rolls', 'short_name': 'ROL'},
    {'name': 'SETS', 'short_name': 'SET'},
    {'name': 'Square Feet', 'short_name': 'SQF'},
    {'name': 'Square Meters', 'short_name': 'SQM'},
    {'name': 'Square Yards', 'short_name': 'SQY'},
    {'name': 'Tablets', 'short_name': 'TBS'},
    {'name': 'Ten Grams', 'short_name': 'TGM'},
    {'name': 'Thousands', 'short_name': 'THD'},
    {'name': 'Tonnes', 'short_name': 'TON'},
    {'name': 'Tubes', 'short_name': 'TUB'},
    {'name': 'US Gallon', 'short_name': 'UGS'},
    {'name': 'Units', 'short_name': 'UNT'},
    {'name': 'Yards', 'short_name': 'YDS'},
    {'name': 'Others', 'short_name': 'OTH'},
]


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        for uom_obj in uom_list:
            uom, created = UOM.objects.get_or_create(short_name=uom_obj['short_name'], name=uom_obj['name'])
        self.stdout.write(self.style.SUCCESS('Created UOMs'))

