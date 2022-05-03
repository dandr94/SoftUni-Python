array = input()

list_array = array.split(', ')
if list_array.pop() == 'wolf':
    print("Please go away and stop eating my sheep")
else:
    list_array_reversed = list_array[::-1]
    for i in range(len(list_array_reversed)):
        if list_array_reversed[i] != "sheep":
            print(f"Oi! Sheep number {i + 1}! You are about to be eaten by a wolf!")


