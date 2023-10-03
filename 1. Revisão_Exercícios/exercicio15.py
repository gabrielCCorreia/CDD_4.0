num1 = int(input("Digite o 1° número inteiro: "))
num2 = int(input("Digite o 2° número inteiro (diferente do primeiro): "))
while num2 == num1:
    num2 = int(input("Erro! Digite um número diferente do primeiro: "))
if num1 < num2:
    print(f"{num1} e {num2}")
else:
    print(f"{num2} e {num1}")