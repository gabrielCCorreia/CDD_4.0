a = []
num = -1
contador = 0

while contador < 10:
    num += 1
    if num % 2 != 0:
        a.append(num)
        contador += 1

print(a)