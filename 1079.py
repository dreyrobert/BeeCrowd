x = int(input())

list = []
for i in range(x):
    list.append(input())

A = list[0]
B = list[1]
C = list[2]
a1, a2, a3 = map(float, A.split())
b1, b2, b3 = map(float, B.split())
c1, c2, c3 = map(float, C.split())

first = ((a1 * 2) + (a2 * 3) + (a3 * 5)) / 10
second = ((b1 * 2) + (b2 * 3) + (b3 * 5)) / 10
third = ((c1 * 2) + (c2 * 3) + (c3 * 5)) / 10

print(f"{first:.1f}\n{second:.1f}\n{third:.1f}")
