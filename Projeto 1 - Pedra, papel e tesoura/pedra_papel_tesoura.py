while True:

    # Jogatina

    jogador_1 = input(f"É a vez do 1° jogador: ")

    while jogador_1 != 'pedra' and jogador_1 != 'papel' and jogador_1 != 'tesoura':
        jogador_1 = input(f"Texto inválido. Digite novamente: ")

    jogador_2 = input(f"É a vez do 2° jogador: ")

    while jogador_2 != 'pedra' and jogador_2 != 'papel' and jogador_2 != 'tesoura':
        jogador_2 = input(f"Texto inválido. Digite novamente: ")

    # Mecanismo

    if jogador_1 == jogador_2:
        print("\nDeu empate.\n")
    elif jogador_1 == 'pedra' and jogador_2 == 'tesoura' or \
            jogador_1 == 'papel' and jogador_2 == 'pedra' or \
            jogador_1 == 'tesoura' and jogador_2 == 'papel':
        print(f"\nO 1° jogador venceu a partida.\n")
    else:
        print(f"\nO 2° jogador venceu a partida.\n")

    # Decisão para encerrar ou continuar o jogo

    decisao = input("Continuar o jogo (s/n)? ")

    while decisao != 's' and decisao != 'n':
        decisao = input("Texto inválido. Digite novamente (s/n): ")
    if decisao == 'n':
        break
    print()

print("\nPrograma finalizado.")