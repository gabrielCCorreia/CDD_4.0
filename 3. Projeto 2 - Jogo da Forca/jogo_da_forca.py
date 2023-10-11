from biblioteca import escolher_palavra

palavra = escolher_palavra()
palavra_escondida = ['_' for x in palavra]
erros_maximos = 6
erros = 0

while True:
    letra = input("Adivinhe uma letra: ").lower()

    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                palavra_escondida[i] = letra
    else:
        erros += 1
        print("Letra não encontrada na palavra.")
        print(f"Erros restantes: {erros_maximos - erros}")

    print(' '.join(palavra_escondida))

    if '_' not in palavra_escondida:
        print("Parabéns! Você ganhou!")
        break

    if erros == erros_maximos:
        print(f"Você perdeu. A palavra era: {palavra}")
        break