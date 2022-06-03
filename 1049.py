list = [0, 0, 0]
for index,value in enumerate(list):
    list[index] = input()

first = list[0]
second = list[1]
third = list[2]

if first == 'vertebrado':
    if second == 'ave':
        if third == 'carnivoro':
            print("aguia")
        else:
            print("pomba")
    else:
        if third == 'onivoro':
            print("homem")
        else:
            print("vaca")

if first == 'invertebrado':
    if second == 'inseto':
        if third == 'hematofago':
            print("pulga")
        else:
            print("lagarta")
    else:
        if third == 'hematofago':
            print("sanguessuga")
        else:
            print("minhoca")

    

