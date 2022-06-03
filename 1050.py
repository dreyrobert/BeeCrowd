s = float(input())

sum = 0
if s > 0 and s <= 2000:
    print("Isento")
    exit()

if s > 2000 and s <= 3000:
    sum = (s - 2000) * 0.08
elif s > 3000 and s <= 4500:
    sum = 80 + (s - 3000) * 0.18
else:
    sum = 270 + 80 + (s - 4500) * 0.28

print(f"R$ {sum:.2f}")



