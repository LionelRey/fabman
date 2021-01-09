# Generated by Django 3.1.4 on 2021-01-09 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_member_visa'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usage',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
            preserve_default=False,
        ),
    ]
