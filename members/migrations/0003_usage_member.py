# Generated by Django 3.1.4 on 2020-12-27 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_resource_usage'),
    ]

    operations = [
        migrations.AddField(
            model_name='usage',
            name='member',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='members.member'),
            preserve_default=False,
        ),
    ]
