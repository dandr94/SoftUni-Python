text = input()


if text == 'Monday' or text == 'Tuesday' or text == 'Wednesday' or text == 'Thursday' or text == 'Friday':
    print('Working day')
elif text == 'Saturday' or text == 'Sunday':
    print('Weekend')
else:
    print('Error')