string_of_elements = input().split(' ')
k = int(input())

result = []
count = 0
index = 0

while string_of_elements:
    count += 1

    if count % k == 0:
        result.append(string_of_elements.pop(index))
    else:
        index += 1

    if index >= len(string_of_elements):
        index = 0
int_list = list(map(int, result))

print(str(int_list).replace(' ', ''))



