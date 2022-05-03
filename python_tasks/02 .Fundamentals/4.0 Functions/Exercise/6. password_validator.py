input_password = input()


def is_valid_length(length):
    is_valid = False

    if 6 <= len(input_password) <= 10:
        is_valid = True

    return is_valid


def is_valid_letters_and_digits(letters_and_digits):
    is_valid = False

    if input_password.isalnum():
        is_valid = True

    return is_valid


def is_valid_digits(digits):
    is_valid = False
    count = 0
    for char in input_password:
        if char.isdigit():
            count += 1
    if count >= 2:
        is_valid = True

    return is_valid


if is_valid_digits(input_password) and is_valid_letters_and_digits(input_password) \
        and is_valid_length(input_password):
    print('Password is valid')
else:
    if not is_valid_length(input_password):
        print('Password must be between 6 and 10 characters')

    if not is_valid_letters_and_digits(input_password):
        print('Password must consist only of letters and digits')

    if not is_valid_digits(input_password):
        print('Password must have at least 2 digits')



