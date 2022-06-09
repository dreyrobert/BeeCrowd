x = int(input())

number = 0
for i in range(x+1):
    if i == 0:
        number += 1
    elif i % 2 == 0:
        print(f'{i}^2 = {(i**2)}')