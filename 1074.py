x = int(input())

list = []
for i in range(x):
    list.append(int(input()))

for index, value in enumerate(list):
    if list[index] == 0:
        print('NULL')
    elif list[index] % 2 == 0:
        if list[index] > 0:
            print('EVEN POSITIVE')
        else:
            print('EVEN NEGATIVE')
    else:
        if list[index] > 0:
            print('ODD POSITIVE')
        else:
            print('ODD NEGATIVE')



