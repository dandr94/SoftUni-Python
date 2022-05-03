from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from my_music_app.web.validators import validate_only_letters_numbers_and_underscore


class Profile(models.Model):
    USERNAME_MIN_CHAR = 2
    USERNAME_MAX_CHAR = 15

    AGE_MIN_VALUE = 0

    username = models.CharField(
        max_length=USERNAME_MAX_CHAR,
        validators=[
            MinLengthValidator(USERNAME_MIN_CHAR),
            validate_only_letters_numbers_and_underscore

        ]
    )

    email = models.EmailField(

    )

    age = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(AGE_MIN_VALUE)
        ]
    )


class Album(models.Model):
    ALBUM_NAME_MAX_CHAR = 30

    ARTIST_MAX_CHAR = 30

    GENRE_MAX_CHAR = 30
    GENRE_CHOICES = [
        ('Pop', 'Pop Music'),
        ('Jazz', 'Jazz Music'),
        ('R&B', 'R&B Music'),
        ('Rock', 'Rock Music'),
        ('Country', 'Country Music'),
        ('Dance', 'Dance Music'),
        ('Hip Hop', 'Hip Hop Music'),
        ('Other', 'Other')
    ]

    PRICE_MIN_VALUE = 0

    album_name = models.CharField(
        unique=True,
        max_length=ALBUM_NAME_MAX_CHAR,
        verbose_name='Album Name'

    )

    artist = models.CharField(
        max_length=ARTIST_MAX_CHAR
    )

    genre = models.CharField(
        max_length=GENRE_MAX_CHAR,
        choices=GENRE_CHOICES
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    image_url = models.URLField(
        verbose_name='Image URL'
    )

    price = models.FloatField(
        validators=[
            MinValueValidator(PRICE_MIN_VALUE)
        ]
    )
