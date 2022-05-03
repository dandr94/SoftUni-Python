digits = input()

digits_list = sorted(str(digits), reverse=True)

string_list = ''.join(digits_list)
print(string_list)

