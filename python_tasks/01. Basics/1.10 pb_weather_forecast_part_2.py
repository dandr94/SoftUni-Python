degrees = float(input())

if degrees >= 26.00 and degrees <= 35.00:
    print('Hot')
elif degrees > 20 and degrees < 26:
    print('Warm')
elif degrees >= 15.00 and degrees <= 20.00:
    print('Mild')
elif degrees >= 12.00 and degrees < 15:
    print('Cool')
elif degrees >= 5.00 and degrees < 12:
    print('Cold')
else:
    print('unknown')