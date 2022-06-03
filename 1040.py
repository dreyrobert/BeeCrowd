get_X = input()
X = get_X.split()
one = float(X[0])
two = float(X[1])
three = float(X[2])
four = float(X[3])

def exame(media):
    print(f"Media: {media:.1f}\nAluno em exame.")
    Y = float(input())
    print(f"Nota do exame: {Y:.1f}")
    newMedia = (media + Y)/2
    if newMedia >= 5:
        print(f"Aluno aprovado.\nMedia final: {newMedia:.1f}")
    else:
        print(f"Aluno reprovado.\nMedia final: {newMedia:.1f}")

media = ((one*2) + (two*3) + (three*4) + four)/10
if media >= 7:
    print(f"Media: {media:.1f}\nAluno aprovado.")
elif media < 5:
    print(f"Media: {media:.1f}\nAluno reprovado.")
else:
    exame(media)