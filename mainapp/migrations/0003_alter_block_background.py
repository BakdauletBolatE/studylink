# Generated by Django 3.2.5 on 2021-07-16 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20210716_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='background',
            field=models.ImageField(blank=True, null=True, upload_to='ImagesStudy/'),
        ),
    ]
