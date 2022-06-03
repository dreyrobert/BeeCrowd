X = float(input())

if X < 0:
    exit()

if X > 0 and X <= 400:
    much = X * 0.15
    new = X + much
    per = 15
elif X > 400 and X <= 800:
    much = X * 0.12
    new = X + much
    per = 12
elif X > 800 and X <= 1200:
    much = X * 0.1
    new = X + much
    per = 10
elif X > 1200 and X <= 2000:
    much = X * 0.07
    new = X + much
    per = 7
else:
    much = X * 0.04
    new = X + much
    per = 4

print(f"Novo salario: {new:.2f}\nReajuste ganho: {much:.2f}\nEm percentual: {per} %")
