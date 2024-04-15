class animal:
    def __int__(self, nome, idade, peso, genero):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.genero = genero
        self.Anda = False
        self.FazBarulho = False

    def Anda(self, destino):
        self.Anda = True
        print(f"{self.nome} anda, então ele é terrestre")

    def FazBarulho(self, som):
        self.FazBarulho = True
        print(f"{self.nome} faz barulho")


class dog(animal):
    def __init__(self, nome, idade, peso, genero, raca, dono, cor):
        super(animal).__init__(nome, idade, peso, genero)
        self.raca = raca
        self.dono = dono
        self.cor = cor
dog1 = dog("Max", "8 meses", "3kg", "Masculino", "Pinscher", "Eloah", "Preto")