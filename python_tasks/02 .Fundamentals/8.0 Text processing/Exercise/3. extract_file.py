file_path = input().split('\\')

needed_things = file_path[-1].split('.')

print(f'File name: {needed_things[0]}')
print(f'File extension: {needed_things[1]}')