# Generated by Django 3.1.5 on 2021-02-11 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0030_auto_20210211_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='civility',
            field=models.CharField(choices=[('Mme', 'Madame'), ('M', 'Monsieur'), ('Non souhaitée', 'Non souhaitée'), ('Association', 'Association'), ('Entreprise', 'Entreprise')], default='no member', max_length=20),
        ),
    ]
