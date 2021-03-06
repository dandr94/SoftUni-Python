# Generated by Django 4.0.2 on 2022-02-27 07:33

import django.core.validators
from django.db import migrations, models
import my_music_app.web.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=30, unique=True)),
                ('artist', models.CharField(max_length=30)),
                ('genre', models.CharField(choices=[('Pop', 'Pop Music'), ('Jazz', 'Jazz Music'), ('R&B', 'R&B Music'), ('Rock', 'Rock Music'), ('Country', 'Country Music'), ('Dance', 'Dance Music'), ('Hip Hop', 'Hip Hop Music'), ('Other', 'Other')], max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('image_url', models.URLField()),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), my_music_app.web.validators.validate_only_letters_numbers_and_underscore])),
                ('email', models.EmailField(max_length=254)),
                ('age', models.ImageField(blank=True, null=True, upload_to='', validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]
