v = int(input())
p_1 = int(input())
p_2 = int(input())
h = float(input())

pipe_1 = h * p_1
pipe_2 = h * p_2
sum = pipe_1 + pipe_2
percent = sum / v * 100
pipe_1_percent = pipe_1 / sum * 100
pipe_2_percent = pipe_2 / sum * 100

if sum <= v:
    print(f'The pool is {percent:.2f}% full. Pipe 1: {pipe_1_percent:.2f}%. Pipe 2: {pipe_2_percent:.2f}%.')
else:
    diff = sum - v
    print(f'For {h:.2f} hours the pool overflows with {diff:.2f} liters.')
