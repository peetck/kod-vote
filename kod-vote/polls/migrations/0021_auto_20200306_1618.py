# Generated by Django 3.0.3 on 2020-03-06 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0020_auto_20200304_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]
