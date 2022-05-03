number_of_pages_in_book = int(input())
pages = int(input())
days = int(input())

time_needed_for_one_book = number_of_pages_in_book / pages
sum = time_needed_for_one_book / days
print(sum)