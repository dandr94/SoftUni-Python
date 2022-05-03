num_1 = int(input())
num_2 = int(input())



for i in range(num_1, num_2 + 1):
    num_to_str = str(i)
    even_sum = 0
    odd_sum = 0
    for position, num in enumerate(num_to_str):
        if position % 2 == 0:
            even_sum += int(num)
        else:
            odd_sum += int(num)

    if odd_sum == even_sum:
        print(num_to_str, end=" ")

