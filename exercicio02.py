continuar = "s"
while continuar == "s":
    num = int(input("Digite um número: "))
    while num == 0:
        num = int(input("Número inválido. Tente novamente: "))
    if num > 0:
        print(f"O número {num} é positivo")
    elif num < 0:
        print(f"O número {num} é negativo")
    continuar = input("Deseja continuar? (s/n): ")
print("Programa finalizado.")