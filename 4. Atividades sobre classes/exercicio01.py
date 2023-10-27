class Pessoa:
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.comida = None
        self.comendo = False
        self.andando = False
        self.dormindo = False

    def comer(self, comida):
        if self.andando:
            print(f"{self.nome} não pode comer enquanto estiver caminhando.")
        elif self.dormindo:
            print(f"{self.nome} não pode comer enquanto estiver dormindo.")
        elif not self.comendo:
            self.comida = comida
            self.comendo = True
            print(f"{self.nome} está comendo {self.comida}.")
        else:
            print(f"{self.nome} já está comendo {self.comida}. Para comer {comida}, pare de comer primeiro.")

    def pararComer(self):
        if self.comendo:
            self.comendo = False
            print(f"{self.nome} parou de comer.")
        else:
            print(f"{self.nome} não está comendo atualmente.")

    def andar(self):
        if self.comendo:
            print(f"{self.nome} não pode caminhar enquanto estiver comendo.")
        elif self.dormindo:
            print(f"{self.nome} não pode caminhar enquanto estiver dormindo.")
        elif not self.andando:
            self.andando = True
            print(f"{self.nome} está caminhando.")
        else:
            print(f"{self.nome} já está caminhando.")

    def pararAndar(self):
        if self.andando:
            self.andando = False
            print(f"{self.nome} parou de caminhar.")
        else:
            print(f"{self.nome} não está caminhando atualmente.")

    def dormir(self):
        if self.andando:
            print(f"{self.nome} não pode dormir enquanto estiver caminhando.")
        elif self.comendo:
            print(f"{self.nome} não pode dormir enquanto estiver comendo.")
        elif not self.dormindo:
            self.dormindo = True
            print(f"{self.nome} está dormindo.")
        else:
            print(f"{self.nome} já está dormindo.")

    def acordar(self):
        if self.dormindo:
            self.dormindo = False
            print(f"{self.nome} acordou.")
        else:
            print(f"{self.nome} já está acordado(a).")


p1 = Pessoa("Ranna", 19, 48)
p1.comer("frutas")
p1.comer("vegetais")
p1.pararComer()
p1.pararComer()
print()
p1.andar()
p1.andar()
p1.pararAndar()
p1.pararAndar()
print()
p1.dormir()
p1.dormir()
p1.acordar()
p1.acordar()
print()
p1.comer("frutas")
p1.comer("vegetais")
p1.andar()
p1.dormir()
p1.pararComer()
print()
p1.andar()
p1.comer("legumes")
p1.dormir()
p1.pararAndar()
print()
p1.dormir()
p1.andar()
p1.comer("feijão")
p1.acordar()