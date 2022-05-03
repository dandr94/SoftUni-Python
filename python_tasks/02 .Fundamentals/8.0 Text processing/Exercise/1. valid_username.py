usernames = input().split(', ')


for i in usernames:
    if 2 < len(i) <= 16:
        if i.isalnum() or '-' in i or '_' in i:
            print(i)