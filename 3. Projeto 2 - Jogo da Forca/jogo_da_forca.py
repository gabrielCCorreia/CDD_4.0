from biblioteca import *

palavra = escolher_palavra()
palavra_escondida = ['_' for x in palavra]
erros_maximos = 7
erros = 0
repeticao = True

while True:

    if repeticao:
        bonequinho_forca(erros)
        print(' '.join(palavra_escondida))
    repeticao = True

    letra = input("Adivinhe uma letra: ").lower()

    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                palavra_escondida[i] = letra
    else:
        erros += 1
        bonequinho_forca(erros)
        print(' '.join(palavra_escondida))
        repeticao = False
        print("Letra não encontrada na palavra.")
        print(f"Erro(s) restante(s): {erros_maximos - erros}")

    if '_' not in palavra_escondida:
        bonequinho_forca(erros)
        print(' '.join(palavra_escondida))
        print("Parabéns! Você ganhou!")
        break

    if erros == erros_maximos:
        print(f"Você perdeu. A palavra era: {palavra}")
        break
