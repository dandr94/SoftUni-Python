from django.db import models


class Recipe(models.Model):
    TITLE_MAX_CHAR = 30
    INGREDIENTS_MAX_CHAR = 250

    title = models.CharField(
        max_length=TITLE_MAX_CHAR
    )

    image = models.URLField(
        verbose_name='Image URL'
    )

    description = models.TextField(

    )

    ingredients = models.CharField(
        max_length=INGREDIENTS_MAX_CHAR
    )

    time = models.IntegerField(
        verbose_name='Time (Minutes)'

    )

    @property
    def full_ingredients(self):
        all_ingredients = self.ingredients.split(', ')
        return all_ingredients
