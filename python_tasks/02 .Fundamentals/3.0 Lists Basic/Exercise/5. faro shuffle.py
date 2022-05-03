cards = input().split()
shuffle = int(input())
# get the new solution. It is a lot better!!!
length_of_the_deck = len(cards)
middle_of_the_deck = int(length_of_the_deck / 2)
final_shuffle = []
for i in range(0, shuffle):
    new_list = []
    for p in range(0, middle_of_the_deck):
        new_list.append(cards[p])
        new_list.append(cards[middle_of_the_deck])
        middle_of_the_deck += 1
    cards = new_list
    middle_of_the_deck = int(length_of_the_deck / 2)
    final_shuffle = new_list

print(final_shuffle)




