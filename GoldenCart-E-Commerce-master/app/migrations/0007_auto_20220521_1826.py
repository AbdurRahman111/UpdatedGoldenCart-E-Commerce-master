# Generated by Django 3.0.8 on 2022-05-21 12:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20220521_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='Days',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='End_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 5, 21, 18, 26, 46, 226277), null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='Start_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 5, 21, 18, 26, 46, 226277), null=True),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='Days',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='End_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 5, 21, 18, 26, 46, 227273), null=True),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='Start_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 5, 21, 18, 26, 46, 227273), null=True),
        ),
    ]