# Generated by Django 4.2.4 on 2023-09-14 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('age_calculator_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agecalculator',
            name='birthday_date',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
