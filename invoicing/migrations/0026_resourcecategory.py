# Generated by Django 3.1.5 on 2021-01-16 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing', '0025_auto_20210112_2108'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
