start = ord(input())
end = ord(input())
some_text = input()

sum_of_char = 0

for i in some_text:
    if start < ord(i) < end:
        sum_of_char += ord(i)

print(sum_of_char)

