gifts = input().split(' ')

action = input().split(' ')
while action[0] != 'No' and action[1] != 'Money':
    product = action[1]
    index = 0
    if action[0] == 'OutOfStock':
        while product in gifts:
            index = gifts.index(product)
            gifts[index] = 'None'

    elif action[0] == 'Required':
        index = int(action[2])
        if 0 < index < len(gifts):
            gifts[index] = action[1]

    elif action[0] == 'JustInCase':
        gifts[-1] = action[1]

    action = input().split(' ')

while 'None' in gifts:
    gifts.remove('None')

final_result = ' '.join(gifts)
print(final_result)