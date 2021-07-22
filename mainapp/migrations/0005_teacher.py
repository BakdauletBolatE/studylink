# Generated by Django 3.2.5 on 2021-07-22 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_block_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='teacherImages/')),
                ('experiense', models.CharField(max_length=255)),
                ('education', models.CharField(max_length=255)),
                ('formAction', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
