# Generated by Django 4.0.2 on 2022-02-23 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.URLField(verbose_name='Image URL'),
        ),
    ]