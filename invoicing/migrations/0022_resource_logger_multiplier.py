# Generated by Django 3.1.5 on 2021-01-12 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing', '0021_usage_unit_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='logger_multiplier',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
        ),
    ]