x = int(input())
list = [0]

i = 0
temp = 0
while i < x:
    temp = int(input())
    list.append(temp)
    i += 1

list.sort()

count = 0
for i in range(x):
    if list[i] >= 10 and list[i] <= 20:
        count += 1

others = x - count

print(f"""{count} in
{others} out""")