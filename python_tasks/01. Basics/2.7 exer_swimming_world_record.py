import math
record_in_sec = float(input())
length_in_m = float(input())
time_in_sec_for_m = float(input())


needed_time = length_in_m * time_in_sec_for_m
resistance = math.floor(length_in_m / 15) * 12.5
sum_time = needed_time + resistance

if sum_time < record_in_sec:
    print(f'Yes, he succeeded! The new world record is {sum_time:.2f} seconds.')
else:
    diff = sum_time - record_in_sec
    print(f'No, he failed! He was {diff:.2f} seconds slower.')