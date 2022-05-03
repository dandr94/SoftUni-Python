from project.worker import Worker


class Vet(Worker):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)



    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"