number_of_electrons = int(input())

left_electrons = 0

electron_list = []
count = 1
while number_of_electrons > 0:
    electron_by_index = 2 * (count ** 2)
    count += 1

    if number_of_electrons >= electron_by_index:
        number_of_electrons -= electron_by_index
        electron_list.append(electron_by_index)
    else:
        remainder = abs(electron_by_index - number_of_electrons)
        result = electron_by_index - remainder
        number_of_electrons -= result
        electron_list.append(result)

print(electron_list)