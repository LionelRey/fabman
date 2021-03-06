# Generated by Django 3.1.5 on 2021-01-18 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0026_auto_20210118_2135'),
        ('invoicing', '0031_resource_on_submit'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('date', models.DateTimeField()),
                ('comment', models.CharField(blank=True, max_length=200)),
                ('topaye', models.BooleanField(default=True)),
                ('processed', models.BooleanField(default=True)),
                ('expense_type', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='invoicing.expensetype')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='members.member')),
            ],
        ),
    ]
