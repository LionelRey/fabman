# Generated by Django 3.1.4 on 2021-01-09 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_member_rfid'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='visa',
            field=models.CharField(default='', max_length=3),
            preserve_default=False,
        ),
    ]
