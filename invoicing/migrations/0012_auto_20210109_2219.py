# Generated by Django 3.1.5 on 2021-01-09 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing', '0011_invoice_invoice_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_number',
            field=models.DecimalField(decimal_places=0, max_digits=6),
        ),
    ]
