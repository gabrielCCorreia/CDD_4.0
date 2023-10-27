class Animal:
    def __init__(self, nome , cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f'A(O) {self.nome} foi comer...')


class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def miar(self):
        print(f'A(O) {self.nome} foi miando...')


class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def latir(self):
        print(f'A(O) {self.nome} foi latindo...')


class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def guinchar(self):
        print(f'A(O) {self.nome} foi guinchando...')


class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def mugir(self):
        print(f'A(O) {self.nome} foi mugindo...')


a1 = Gato("gato", "branco")
a1.miar()

a2 = Cachorro("cachorro", "preto")
a2.latir()

a3 = Coelho("coelho", "malhado com branco e preto")
a3.guinchar()

a4 = Vaca("vaca", "malhado com branco e preto")
a4.mugir()