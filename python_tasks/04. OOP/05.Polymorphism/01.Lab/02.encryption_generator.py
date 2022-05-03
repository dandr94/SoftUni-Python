class EncryptionGenerator:
    def __init__(self, text):
        self.text = text

    def __add__(self, other):
        if not isinstance(other, int):
            return ValueError('You must add a number.')

        result = ''

        for letter in self.text:
            new_letter = ord(letter) + other

            while new_letter < 32:
                new_letter += 95
            while new_letter > 126:
                new_letter -= 95

            result += chr(new_letter)

        return result


some_text = EncryptionGenerator('I Love Python!')
print(some_text + 1)
print(some_text + (-1))
