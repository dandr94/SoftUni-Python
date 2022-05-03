box_of_clothes = [int(x) for x in input().split()]
capacity = int(input())
sum_of_racks = 0
racks_used = 0

while box_of_clothes:
    if sum_of_racks + box_of_clothes[-1] < capacity:
        sum_of_racks += box_of_clothes.pop()
    elif sum_of_racks + box_of_clothes[-1] == capacity:
        sum_of_racks += box_of_clothes.pop()
        sum_of_racks = 0
        racks_used += 1
    else:
        racks_used += 1
        sum_of_racks = 0

    if not box_of_clothes and sum_of_racks:
        racks_used += 1

print(racks_used)