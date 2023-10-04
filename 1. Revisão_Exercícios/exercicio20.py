num = []

for x in range(10):
    num.append(int(input(f"Digite o {x + 1}° número: ")))

impares = 0
print("\nÍmpare(s): ", end="")
for x in range(10):
    if num[x] % 2 != 0:
        print(num[x], end=" ")
        impares += 1
if impares > 0:
    print(f"// O array possui {impares} número(s) ímpare(s)")
else:
    print(f"Nenhum")

pares = 0
print("\nPare(s): ", end="")
for x in range(10):
    if num[x] % 2 == 0:
        print(num[x], end=" ")
        pares += 1
if pares > 0:
    print(f"// O array possui {pares} número(s) pare(s)")
else:
    print(f"Nenhum")

positivos = 0
print("\nPositivo(s): ", end="")
for x in range(10):
    if num[x] >= 0:
        print(num[x], end=" ")
        positivos += 1
if positivos > 0:
    print(f"// O array possui {positivos} número(s) positivo(s)")
else:
    print(f"Nenhum")

negativos = 0
print("\nNegativo(s): ", end="")
for x in range(10):
    if num[x] < 0:
        print(num[x], end=" ")
        negativos += 1
if negativos > 0:
    print(f"// O array possui {negativos} número(s) negativo(s)")
else:
    print(f"Nenhum")

zeros = 0
print("\nZero(s): ", end="")
for x in range(10):
    if num[x] == 0:
        print(num[x], end=" ")
        zeros += 1
if zeros > 0:
    print(f"// O array possui {zeros} número(s) zero(s)")
else:
    print(f"Nenhum")