x, y = map(float, input().split())

if x > 0 and y > 0:
    print("Q1")
elif x > 0 and y < 0:
    print("Q4")
elif x < 0 and y < 0:
    print("Q3")
elif x < 0 and y > 0:
    print("Q2")
else:
    if x == y == 0:
        print("Origem")
    if x == 0 and y != 0:
        print("Eixo Y")
    if x != 0 and y == 0:
        print("Eixo X")
