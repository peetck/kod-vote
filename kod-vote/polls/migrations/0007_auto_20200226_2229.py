# Generated by Django 3.0.3 on 2020-02-26 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20200226_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='password',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
