money = float(input())

cedulas = [100, 50, 20, 10, 5, 2, 1]
numbers = [0, 0, 0, 0, 0, 0, 0]

resto = int(money)
resto2 = money - resto

for index, value in enumerate(cedulas):
    numbers[index] = resto // cedulas[index]
    resto = resto - (numbers[index] * cedulas[index])

moeda = [0.5, 0.25, 0.1, 0.05, 0.01]
numbers2 = [0, 0, 0, 0, 0]

for index, value in enumerate(moeda):
    numbers2[index] = resto2 // moeda[index]
    resto2 = resto2 - (numbers2[index] * moeda[index])

print("""NOTAS:
{numbers[0]} nota(s) de R$ {cedulas[0}.00
{numbers[1]} nota(s) de R$ {cedulas[1}.00
{numbers[2]} nota(s) de R$ {cedulas[2}.00
{numbers[3]} nota(s) de R$ {cedulas[3}.00
{numbers[4]} nota(s) de R$ {cedulas[4}.00
{numbers[5]} nota(s) de R$ {cedulas[5}.00
{numbers[6]} nota(s) de R$ {cedulas[6}.00
MOEDAS:
{numbers2[0]} moeda(s) de R$ {cedulas[7]}.00
{numbers2[1]} moeda(s) de R$ {moeda[0]}.00
{numbers2[2]} moeda(s) de R$ {moeda[1]}.00
{numbers2[3]} moeda(s) de R$ {moeda[2]}.00
{numbers2[4]} moeda(s) de R$ {moeda[3]}.00
{numbers2[5]} moeda(s) de R$ {moeda[4]}.00""")
