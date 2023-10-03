hora_inicio = int(input("Digite a hora de início do jogo: "))
hora_fim = int(input("Digite a hora de fim do jogo: "))
if hora_inicio <= hora_fim:
    duracao = hora_fim - hora_inicio
else:
    duracao = (24 - hora_inicio) + hora_fim
print(f"A duração do jogo de xadrez foi de {duracao} horas.")