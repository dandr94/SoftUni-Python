main_mats = {'shards': 0, 'motes': 0, 'fragments': 0}
junk = {}

not_collected = True

while not_collected:
    cmd = input().split()

    for i in range(0, len(cmd), 2):
        item = cmd[i + 1].lower()
        quantity = int(cmd[i])

        if item == 'shards' or item == 'fragments' or item == 'motes':
            main_mats[item] += quantity
            if main_mats[item] >= 250:
                if item == 'shards':
                    print('Shadowmourne obtained!')
                elif item == 'fragments':
                    print('Valanyr obtained!')
                elif item == 'motes':
                    print('Dragonwrath obtained!')
                main_mats[item] -= 250
                not_collected = False
                break
        else:
            if item not in junk:
                junk[item] = 0
            junk[item] += quantity


for key, value in sorted(main_mats.items(), key=lambda x: (-x[1], x[0])):
    print(f'{key}: {value}')
for key, value in sorted(junk.items(), key=lambda x: x[0]):
    print(f'{key}: {value}')

