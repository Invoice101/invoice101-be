# Generated by Django 3.0.5 on 2020-04-18 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='betasubscription',
            name='email',
            field=models.EmailField(max_length=500, unique=True),
        ),
    ]
