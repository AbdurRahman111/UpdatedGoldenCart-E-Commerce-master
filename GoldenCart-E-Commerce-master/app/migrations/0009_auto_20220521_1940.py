# Generated by Django 3.0.8 on 2022-05-21 13:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20220521_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='Days',
            field=models.PositiveIntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='End_date',
            field=models.CharField(blank=True, default=datetime.datetime(2022, 5, 21, 19, 40, 40, 11822), max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='Start_date',
            field=models.CharField(blank=True, default=datetime.datetime(2022, 5, 21, 19, 40, 40, 11822), max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='End_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 5, 21, 19, 40, 40, 11822), null=True),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='Start_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 5, 21, 19, 40, 40, 11822), null=True),
        ),
    ]