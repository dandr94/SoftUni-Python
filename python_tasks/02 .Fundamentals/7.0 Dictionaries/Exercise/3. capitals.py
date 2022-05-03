country_names = input().split(', ')
capitals = input().split(', ')

my_dict = dict(zip(country_names, capitals))


for key, value in my_dict.items():
    print(f'{key} -> {value}')