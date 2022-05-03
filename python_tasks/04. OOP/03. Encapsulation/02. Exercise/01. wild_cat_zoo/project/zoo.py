from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if price > self.__budget:
            return 'Not enough budget'
        if len(self.animals) == self.__animal_capacity:
            return 'Not enough space for animal'

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) == self.__workers_capacity:
            return 'Not enough space for worker'

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        sum_of_salaries = 0
        for worker in self.workers:
            sum_of_salaries += worker.salary

        if sum_of_salaries <= self.__budget:
            self.__budget -= sum_of_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return f'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        sum_of_care_money = 0
        for animal in self.animals:
            sum_of_care_money += animal.money_for_care

        if sum_of_care_money <= self.__budget:
            self.__budget -= sum_of_care_money
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return 'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        output = f'You have {len(self.animals)} animals'
        my_dict = {'Lion': [],
                   'Tiger': [],
                   'Cheetah': []}

        for animal in self.animals:
            my_dict[animal.__class__.__name__].append(animal)

        for class_name, all_animals in my_dict.items():
            output += f'\n----- {len(all_animals)} {class_name}s:'
            for animal_name in all_animals:
                output += '\n'
                output += f'{animal_name}'

        return output

    def workers_status(self):
        output = f'You have {len(self.workers)} workers'
        my_dict = {'Keeper': [],
                   'Caretaker': [],
                   'Vet': []}

        for worker in self.workers:
            my_dict[worker.__class__.__name__].append(worker)

        for class_name, all_workers in my_dict.items():
            output += f'\n----- {len(all_workers)} {class_name}s:'
            for worker_name in all_workers:
                output += '\n'
                output += f'{worker_name}'

        return output
