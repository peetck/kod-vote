# Generated by Django 3.0.3 on 2020-03-04 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_auto_20200304_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='password',
            field=models.CharField(default=None, max_length=255),
        ),
    ]