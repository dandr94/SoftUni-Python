words = input().split()
palindrome = input()

palindrome_list = []

# [el for el in words if el == el[::-1]

for i in words:
    if i == ''.join(reversed(i)):
        palindrome_list.append(i)

print(palindrome_list)
print(f'Found palindrome {palindrome_list.count(palindrome)} times')




