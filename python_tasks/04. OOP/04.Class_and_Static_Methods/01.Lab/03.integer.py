import roman


class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return f'value is not a float'
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value):
        result = roman.fromRoman(value)

        return cls(result)

    @classmethod
    def from_string(cls, value):
        try:
            return cls(int(value))
        except:
            return 'wrong type'


first_num = Integer(10)
second_num = Integer.from_roman("IV")

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
