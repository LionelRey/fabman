# Generated by Django 3.1.5 on 2021-02-11 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0029_auto_20210211_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='npa',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone_number',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
