list = [0, 0]
for i in range(0,2):
    list[i] = int(input())

list.sort()
if list[0] < 0:
    list[0] += 1
    
sum = 0
while list[0] + 1 <= list[1]:
    if list[0] % 2 != 0:
        sum += list[0]
    list[0] += 1

print(sum)