# Generated by Django 3.0.3 on 2020-02-26 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20200226_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='picture',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='poll_choice',
            name='image',
            field=models.ImageField(default='default_choice.jpg', upload_to=''),
        ),
    ]
