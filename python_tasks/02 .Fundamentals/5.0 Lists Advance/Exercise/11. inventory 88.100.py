collection_of_items = input().split(', ')

command = input()

while command != 'Craft!':
    command_split = command.split(' - ')
    action = command_split[0]

    if action == 'Collect':
        item = command_split[1]
        if item not in collection_of_items:
            collection_of_items.append(item)

    elif action == 'Drop':
        item = command_split[1]
        if item in collection_of_items:
            while item in collection_of_items:
                collection_of_items.remove(item)
    elif action == 'Combine Items':
        items = command_split[1].split(':')
        old_item = items[0]
        new_item = items[1]
        old_item_index = collection_of_items.index(old_item)
        if old_item in collection_of_items:
            collection_of_items.insert(old_item_index + 1, new_item)
    elif action == 'Renew':
        item = command_split[1]
        if item in collection_of_items:
            item_index = collection_of_items.index(item)
            collection_of_items.append(collection_of_items.pop(item_index))

    command = input()

print(', '.join(collection_of_items))
