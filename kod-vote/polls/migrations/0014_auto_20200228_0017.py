# Generated by Django 3.0.3 on 2020-02-27 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20200227_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll_choice',
            name='image',
            field=models.ImageField(default='choice/default.png', upload_to='choice/'),
        ),
    ]