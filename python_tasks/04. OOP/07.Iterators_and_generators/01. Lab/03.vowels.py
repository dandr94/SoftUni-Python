class vowels:
    def __init__(self, my_string: str):
        self.my_string = my_string
        self.all_vowels = 'AaEeIiOoUuYy'
        self.my_vowels = [x for x in self.my_string if x in self.all_vowels]
        self.start = 0
        self.end = len(self.my_vowels) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration

        current = self.start
        self.start += 1
        return self.my_vowels[current]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
