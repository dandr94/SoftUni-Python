from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from expenses_tracker.web.validators import only_letters_validator, MaxFileSizeInMbValidator


class Profile(models.Model):
    FIRST_NAME_MIN_CHAR = 2
    FIRST_NAME_MAX_CHAR = 15

    LAST_NAME_MIN_CHAR = 2
    LAST_NAME_MAX_CHAR = 30

    BUDGET_DEFAULT_VALUE = 0
    BUDGET_BOTTOM_LIMIT = 0

    IMAGE_MAX_SIZE_IN_MB = 5

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_CHAR,
        validators=[only_letters_validator,
                    MinLengthValidator(FIRST_NAME_MIN_CHAR)

                    ],
        verbose_name='First Name'
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_CHAR,
        validators=[only_letters_validator,
                    MinLengthValidator(LAST_NAME_MIN_CHAR)],
        verbose_name='Last Name'
    )

    budget = models.FloatField(
        default=BUDGET_DEFAULT_VALUE,
        validators=[
            MinValueValidator(BUDGET_BOTTOM_LIMIT)

        ]
    )

    image = models.ImageField(
        blank=True,
        null=True,
        validators=[
            MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB)
        ],
        verbose_name='Profile Image'
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Expense(models.Model):
    TITLE_MAX_CHAR = 30

    title = models.CharField(
        max_length=TITLE_MAX_CHAR
    )

    image = models.URLField(
        verbose_name='Link to Image'
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    price = models.FloatField(

    )
