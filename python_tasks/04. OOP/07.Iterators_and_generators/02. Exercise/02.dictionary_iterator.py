class dictionary_iter:
    def __init__(self, my_dict: dict):
        self.my_dict = my_dict
        self.start = 0
        self.end = len(my_dict) - 1
        self.keys = my_dict.keys()

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration

        current_key = list(self.keys)[self.start]
        self.start += 1
        return current_key, self.my_dict[current_key]

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

