sec_1 = int(input())
sec_2 = int(input())
sec_3 = int(input())


final_time = sec_1 + sec_2 + sec_3

minutes = final_time // 60
seconds = final_time % 60


if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')
