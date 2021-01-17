# Generated by Django 3.1.5 on 2021-01-16 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing', '0027_auto_20210116_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='logger_multiplier',
            field=models.DecimalField(decimal_places=3, default=1, max_digits=9),
        ),
        migrations.AlterField(
            model_name='resource',
            name='price_member',
            field=models.DecimalField(decimal_places=3, max_digits=9),
        ),
        migrations.AlterField(
            model_name='resource',
            name='price_not_member',
            field=models.DecimalField(decimal_places=3, max_digits=9),
        ),
    ]
