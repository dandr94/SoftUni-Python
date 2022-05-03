class sequence_repeat:
    def __init__(self, seq, number):
        self.seq = seq
        self.number = number
        self.start = 0
        self.idx = 0



    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.number:
            raise StopIteration

        current_letter = self.seq[self.idx]
        self.idx += 1
        if self.idx >= len(self.seq):
            self.idx = 0

        self.start += 1
        return current_letter


result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')
