from django.core.exceptions import ValidationError
import re
USERNAME_ONLY_LETTERS_NUMBERS_AND_UNDERSCORE_ERROR_MESSAGE = \
    'Ensure this value contains only letters, numbers, and underscore.'


def validate_only_letters_numbers_and_underscore(value):
    is_valid = re.match(r'^[a-zA-Z0-9_]*$', value)

    if not is_valid:
        raise ValidationError(USERNAME_ONLY_LETTERS_NUMBERS_AND_UNDERSCORE_ERROR_MESSAGE)
