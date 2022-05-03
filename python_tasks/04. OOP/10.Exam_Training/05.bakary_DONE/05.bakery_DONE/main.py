from project.baked_food.cake import Cake
from project.bakery import Bakery
from project.table.inside_table import InsideTable
from project.table.table import Table


bakery = Bakery('Foo')

# print(bakery.add_table('InsideTable', 33, 50))
# print(bakery.add_food('Cake', 'Mite', 25))
# print(bakery.add_food('Cake', 'Mitko', 35))
# print(bakery.add_food('Bread', 'Foo', 5))
# print(bakery.add_food('Bread', 'Bar', 2))
print(bakery.add_table('InsideTable', 33, 50))
print(bakery.add_drink('Tea', 'Mite', 25, 'Foobar'))
print(bakery.add_drink('Tea', 'Mitko', 35, 'Kaspichan'))
print(bakery.add_drink('Water', 'Foo', 5, 'Boiko'))
print(bakery.order_drink(33, 'Mite', 'Mitko', 'Batko', 'Vladko', 'Foo'))
print(bakery.leave_table(33))
print(bakery.get_free_tables_info())
print(bakery.get_total_income())





