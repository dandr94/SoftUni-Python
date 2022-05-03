def is_valid_index(index: int):
    if 0 <= index < len(cards):
        return True

    return False


cards = input().split(':')
deck = []
cmd = input()

while cmd != 'Ready':
    cmd_split = cmd.split()
    action = cmd_split[0]

    if action == 'Add':
        card_name = cmd_split[1]

        if card_name not in cards:
            print('Card not found.')
        else:
            deck.append(card_name)

    elif action == 'Insert':
        card_name = cmd_split[1]
        index = int(cmd_split[2])

        if card_name not in cards or not is_valid_index(index):
            print('Error!')
        else:
            deck.insert(index, card_name)

    elif action == 'Remove':
        card_name = cmd_split[1]

        if card_name not in deck:
            print('Card not found.')
        else:
            deck.remove(card_name)

    elif action == 'Swap':
        card_name_1 = deck.index(cmd_split[1])
        card_name_2 = deck.index(cmd_split[2])

        deck[card_name_1], deck[card_name_2] = deck[card_name_2], deck[card_name_1]

    elif action == 'Shuffle' and cmd_split[1] == 'deck':
        deck = deck[::-1]

    cmd = input()
print(' '.join(deck))