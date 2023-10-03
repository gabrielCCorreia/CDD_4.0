eleitores = int(input("Digite o número total de eleitores: "))
brancos = int(input("Digite o número de votos brancos: "))
nulos = int(input("Digite o número de votos nulos: "))
validos = int(input("Digite o número de votos válidos: "))
print(f"Votos brancos: {(brancos / eleitores) * 100}%\n"
      f"Votos nulos: {(nulos / eleitores) * 100}%\n"
      f"Votos válidos: {(validos / eleitores) * 100}%\n")