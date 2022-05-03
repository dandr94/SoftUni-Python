from django.db import models


class Profile(models.Model):
    FIRST_NAME_MAX_CHAR = 30

    LAST_NAME_MAX_CHAR = 30

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_CHAR
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_CHAR
    )

    image = models.URLField(
        verbose_name='Image URL'

    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    TITLE_MAX_CHAR = 30

    TYPE_MAX_CHAR = 30

    title = models.CharField(
        max_length=TITLE_MAX_CHAR
    )

    description = models.TextField(

    )

    image = models.URLField(

    )

    type = models.CharField(
        max_length=TYPE_MAX_CHAR
    )
