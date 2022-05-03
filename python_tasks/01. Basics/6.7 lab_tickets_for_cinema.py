movie_name = input()

student_tickets_all = 0
standard_tickets_all = 0
kids_tickets_all = 0
students_per_movie = 0
standard_per_movie = 0
kids_per_movie = 0
tickets_sold = 0


while movie_name != 'Finish':
    free_spaces = int(input())
    while free_spaces > 0:
        type_ticket = input()

        if type_ticket == 'student':
            students_per_movie += 1
        elif type_ticket == 'standard':
            standard_per_movie += 1
        elif type_ticket == 'kid':
            kids_per_movie += 1
        else:
            break
        tickets_sold += 1
        free_spaces -= 1

    student_tickets_all += students_per_movie
    standard_tickets_all += standard_per_movie
    kids_tickets_all += kids_per_movie

    percent = (standard_per_movie + students_per_movie + kids_per_movie) / \
              (standard_per_movie + students_per_movie + kids_per_movie + free_spaces)  * 100
    print(f'{movie_name} - {percent:.2f}% full.')
    students_per_movie = 0
    standard_per_movie = 0
    kids_per_movie = 0
    movie_name = input()

print(f'Total tickets: {tickets_sold}')
print(f'{student_tickets_all / tickets_sold * 100:.2f}% student tickets.')
print(f'{standard_tickets_all / tickets_sold * 100:.2f}% standard tickets.')
print(f'{kids_tickets_all / tickets_sold * 100:.2f}% kids tickets.')

