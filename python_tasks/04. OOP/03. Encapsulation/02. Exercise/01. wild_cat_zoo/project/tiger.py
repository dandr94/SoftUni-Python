from project.animal import Animal


class Tiger(Animal):
    def __init__(self, name, gender, age, money_for_care=45):
        super().__init__(name, gender, age, money_for_care)


    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Gender: {self.gender}'
