class Atleta:
    def __init__(self, aposentado, peso):
        self.aposentado = aposentado
        self.peso = peso
        self.tipo = "atleta"

    def aposentar(self):
        self.aposentado = True

    def aquecer(self):
        print(f"O {self.tipo} está aquecendo.")


class Corredor(Atleta):
    def __init__(self, aposentado, peso):
        super().__init__(aposentado, peso)
        self.tipo = "corredor"

    def correr(self):
        print(f"O {self.tipo} está correndo...")


class Nadador(Atleta):
    def __init__(self, aposentado, peso):
        super().__init__(aposentado, peso)
        self.tipo = "nadador"

    def nadar(self):
        print(f"O {self.tipo} está nadando...")


class Ciclista(Atleta):
    def __init__(self, aposentado, peso):
        super().__init__(aposentado, peso)
        self.tipo = "ciclista"

    def pedalar(self):
        print(f"O {self.tipo} está pedalando...")


class TriAtleta(Corredor, Nadador, Ciclista):
    def __init__(self, aposentado, peso):
        super().__init__(aposentado, peso)


corredor = Corredor(False, 70)
nadador = Nadador(False, 60)
ciclista = Ciclista(False, 80)
triatleta = TriAtleta(False, 40)

corredor.correr()
nadador.nadar()
ciclista.pedalar()
triatleta.correr()
