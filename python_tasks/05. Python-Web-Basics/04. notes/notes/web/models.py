import os

from django.db import models


class Profile(models.Model):
    FIRST_NAME_MAX_CHAR = 20
    LAST_NAME_MAX_CHAR = 20

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_CHAR
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_CHAR
    )

    age = models.IntegerField(

    )

    image_url = models.URLField(
        verbose_name='Link to Profile Image'
    )

    @property
    def full_name(self):
        full_name = f'{self.first_name} {self.last_name}'
        return full_name

    @property
    def delete_profile(self):
        Profile.objects.all().delete()



class Note(models.Model):
    TITLE_MAX_CHAR = 30

    title = models.CharField(
        max_length=TITLE_MAX_CHAR
    )

    image_url = models.URLField(
        verbose_name='Link to Image'
    )

    content = models.TextField(

    )
