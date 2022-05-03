key_num = [int(x) for x in input().split()]

some_string = input()

type_flag = False
coordinates_flag = False
counter_flag = 0
while some_string != 'find':
    counter = 0
    decrypted_msg = ''
    treasure = ''
    coordinates = ''

    for i in some_string:
        if counter >= len(key_num):
            counter = 0
        ord_i = ord(i) - key_num[counter]
        decrypted_msg += chr(ord_i)
        counter += 1

    for b in decrypted_msg:
        if b == '&':
            if counter_flag == 0:
                type_flag = True
                counter_flag += 1
                continue
            else:
                type_flag = False
                counter_flag = 0
        elif b == '<':
            coordinates_flag = True
            continue
        elif b == '>':
            coordinates_flag = False

        if type_flag:
            treasure += b
        if coordinates_flag:
            coordinates += b

    else:
        print(f'Found {treasure} at {coordinates}')
    some_string = input()





