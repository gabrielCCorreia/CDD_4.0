quantidade_macas = int(input("Digite o número de maçãs: "))
if quantidade_macas < 12:
    print(f"O custo total da compra é de R$ {quantidade_macas * 1.30}")
else:
    print(f"O custo total da compra é de R$ {quantidade_macas * 1.00}")