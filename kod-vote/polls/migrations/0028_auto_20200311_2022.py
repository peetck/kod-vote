# Generated by Django 3.0.3 on 2020-03-11 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0027_auto_20200311_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll_choice',
            name='image',
            field=models.ImageField(default='choice/choice_default.gif', upload_to='choice/'),
        ),
    ]
