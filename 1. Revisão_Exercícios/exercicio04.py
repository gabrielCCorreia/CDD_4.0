num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
num3 = int(input("Digite o 3º número: "))
if num1 > num2:
    if num1 > num3:
        print(f"O 1º número (o {num1}) é maior entre eles")
    else:
        print(f"O 3º número (o {num3}) é maior entre eles")
elif num2 > num3:
    print(f"O 2º número (o {num2}) é maior entre eles")
else:
    print(f"O 3º número (o {num3}) é maior entre eles")