class Forma:
    def __init__(self):
        self.area = 0
        self.perimetro = 0

class Retangulo(Forma):
    def __init__(self, comprimento, largura):
        super().__init__()
        self.comprimento = comprimento
        self.largura = largura

    def calculaArea(self):
        self.area = self.comprimento * self.largura

    def calculaPerimetro(self):
        self.perimetro = 2 * (self.comprimento + self.largura)

class Triangulo(Forma):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura

    def calculaArea(self):
        self.area = 0.5 * self.base * self.altura

    def calculaPerimetro(self):
        # Perímetro de um triângulo não é diretamente calculado com base e altura
        # Normalmente, você precisaria de informações adicionais, como os lados.
        self.perimetro = None


# Criando objetos das classes Retangulo e Triangulo
retangulo = Retangulo(4, 5)
triangulo = Triangulo(6, 8)

# Verificando se os objetos são instâncias da classe Forma
print(isinstance(retangulo, Forma))  # True
print(isinstance(triangulo, Forma))  # True

# Calculando a área das formas
retangulo.calculaArea()
triangulo.calculaArea()

# Exibindo os resultados
print(f'Área do retângulo: {retangulo.area}')
print(f'Área do triângulo: {triangulo.area}')
