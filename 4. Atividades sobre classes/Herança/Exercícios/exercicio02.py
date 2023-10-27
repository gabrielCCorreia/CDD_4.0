class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    def imprimeValor(self):
        print(f'Valor do ingresso: R${self.valor:.2f}')


class VIP(Ingresso):
    def __init__(self, valor, adicional):
        super().__init__(valor)
        self.adicional = adicional

    def valorVIP(self):
        return self.valor + self.adicional


# Criando um ingresso com valor básico
ingresso_comum = Ingresso(50.00)
ingresso_comum.imprimeValor()

# Criando um ingresso VIP com valor adicional
ingresso_vip = VIP(80.00, 20.00)
ingresso_vip.imprimeValor()

# Obtendo o valor total do ingresso VIP
total_vip = ingresso_vip.valorVIP()
print(f'Valor do ingresso VIP: R${total_vip:.2f}')