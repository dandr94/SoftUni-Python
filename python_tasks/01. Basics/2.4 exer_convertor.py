num = float(input())
entry = input()
exit = input()

mm_to_cm = num / 10
mm_to_m = num / 1000
cm_to_mm = num * 10
cm_to_m = num / 100
m_to_cm = num * 100
m_to_mm = num * 1000

if entry == 'mm':
    if exit == 'm':
        print(f'{mm_to_m:.3f}')
    else:
        print(f'{mm_to_cm:.3f}')
elif entry == 'cm':
    if exit == 'm':
        print(f'{cm_to_m:.3f}')
    else:
        print(f'{cm_to_mm:.3f}')
elif entry == 'm':
    if exit == 'cm':
        print(f'{m_to_cm:.3f}')
    else:
        print(f'{m_to_mm:.3f}')



