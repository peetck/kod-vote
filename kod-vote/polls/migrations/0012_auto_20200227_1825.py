# Generated by Django 3.0.3 on 2020-02-27 11:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20200227_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
