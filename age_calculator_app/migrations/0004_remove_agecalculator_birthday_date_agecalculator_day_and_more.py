# Generated by Django 4.2.4 on 2023-09-15 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('age_calculator_app', '0003_alter_agecalculator_birthday_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agecalculator',
            name='birthday_date',
        ),
        migrations.AddField(
            model_name='agecalculator',
            name='day',
            field=models.IntegerField(choices=[(8, 8), (17, 17), (27, 27), (20, 20), (29, 29), (22, 22), (13, 13), (18, 18), (2, 2), (11, 11), (4, 4), (30, 30), (5, 5), (14, 14), (7, 7), (16, 16), (23, 23), (9, 9), (1, 1), (24, 24), (25, 25), (26, 26), (10, 10), (19, 19), (3, 3), (12, 12), (21, 21), (28, 28), (6, 6), (31, 31), (15, 15)], default=1, null=True),
        ),
        migrations.AddField(
            model_name='agecalculator',
            name='month',
            field=models.IntegerField(choices=[(3, 'March'), (10, 'October'), (12, 'December'), (9, 'September'), (2, 'February'), (6, 'June'), (7, 'July'), (8, 'August'), (1, 'January'), (4, 'April'), (5, 'May'), (11, 'November')], default=1, null=True),
        ),
        migrations.AddField(
            model_name='agecalculator',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]