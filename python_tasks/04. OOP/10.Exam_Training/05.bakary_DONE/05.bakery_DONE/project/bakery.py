from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError('Name cannot be empty string or white space!')
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        food = self.create_food(food_type, name, price)

        for f in self.food_menu:
            if f.name == name:
                raise Exception(f"{food_type} {name} is already in the menu!")

        self.food_menu.append(food)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: int, brand: str):
        drink = self.create_drink(drink_type, name, portion, brand)

        for d in self.drinks_menu:
            if d.name == name:
                raise Exception(f"{drink_type} {name} is already in the menu!")

        self.drinks_menu.append(drink)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        table = self.create_table(table_type, table_number, capacity)

        for t in self.tables_repository:
            if t.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")

        self.tables_repository.append(table)
        return f'Added table number {table_number} in the bakery'

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        else:
            return f'No available table for {number_of_people} people'

    def order_food(self, table_number: int, *args):
        food_found = []
        food_not_found = []
        table = self.find_table_available(table_number)

        if not table:
            return f'Could not find table {table_number}'

        for food_name in args:
            for food in self.food_menu:
                if food_name == food.name:
                    table.order_food(food)
                    food_found.append(food)
                    break
            else:
                food_not_found.append(food_name)

        return self.give_info_about_orders(self.__name, table_number, food_found, food_not_found)

    def order_drink(self, table_number: int, *args):
        drink_found = []
        drink_not_found = []
        table = self.find_table_available(table_number)

        if not table:
            return f'Could not find table {table_number}'

        for drink_name in args:
            for drink in self.drinks_menu:
                if drink_name == drink.name:
                    table.order_drink(drink)
                    drink_found.append(drink)
                    break
            else:
                drink_not_found.append(drink_name)

        return self.give_info_about_orders(self.__name, table_number, drink_found, drink_not_found)

    def leave_table(self, table_number: int):
        table = self.find_table_available(table_number)
        bill = table.get_bill()
        self.total_income += bill
        table.clear()
        return f'Table: {table_number}\n' \
               f'Bill: {bill:.2f}'

    def get_free_tables_info(self):
        result = ''
        for table in self.tables_repository:
            if not table.is_reserved:
                result += table.free_table_info() + '\n'
        return result.strip()

    def get_total_income(self):
        return f'Total income: {self.total_income:.2f}lv'

    @staticmethod
    def create_food(food_type, name, price):
        if food_type == 'Bread':
            return Bread(name, price)
        if food_type == 'Cake':
            return Cake(name, price)

    @staticmethod
    def create_drink(drink_type: str, name: str, portion: int, brand: str):
        if drink_type == 'Tea':
            return Tea(name, portion, brand)
        if drink_type == 'Water':
            return Water(name, portion, brand)

    @staticmethod
    def create_table(table_type: str, table_number: int, capacity: int):
        if table_type == 'InsideTable':
            return InsideTable(table_number, capacity)
        if table_type == 'OutsideTable':
            return OutsideTable(table_number, capacity)

    def find_table_available(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table

    @staticmethod
    def give_info_about_orders(bakery_name, table_number, list_1, list_2):
        result = ''
        result += f"Table {table_number} ordered:\n"
        for item in list_1:
            result += str(item) + '\n'
        result += f'{bakery_name} does not have in the menu:\n'
        for item in list_2:
            result += f'{item}\n'

        return result.strip()
