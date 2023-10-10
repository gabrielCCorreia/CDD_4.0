a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
impar = 0
cont = 0

while True:
    if cont % 2 != 0:
        a[impar] = cont
        impar += 1
    cont += 1

    if impar >= 10:
        break

print(a)
