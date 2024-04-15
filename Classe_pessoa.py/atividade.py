class pessoa:
    def __init__(self, nome, idade, altura, peso, genero):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.genero = genero
        self.falando = False
        self.andando = False
        self.comendo = False
        self.dormindo = False

    def falar(self, conteudo):
        if self.dormindo == False or self.comendo == False:
            self.falando = True
            print(conteudo)
        elif self.dormindo == True:
            print(f"{self.nome} precisa parar de dormir para falar")
        elif self.comendo == True:
            print(f"{self.nome} precisa parar de comer para falar")

    def pararFalar(self):
        if self.falando == False:
            print(f"{self.nome} não está falando")
        else:
            self.falando = False
            print(f"{self.nome} parou de falar")

    def andar(self, destino):
        if self.dormindo == False:
            self.andando = True
            print("Está andando para " + destino)
        elif self.dormindo == True:
            print(f"{self.nome} precisa parar de dormir para andar")

    def pararAndar(self):
        if self.andando == False:
            print(f"{self.nome} não está andando")
        else:
            self.andando = False
            print(f"{self.nome} parou de andar")
    def comer(self, alimento):
        if self.falando == False or self.dormindo == False:
            self.comendo = True
            print("Está comendo " + alimento)
        elif self.falando == True:
            print(f"{self.nome} precisa parar de falar para comer")
        elif self.dormindo == True:
            print(f"{self.nome} precisa acordar para comer")

    def pararComer(self):
        if self.comendo == False:
            print(f"{self.nome} não está comendo")
        else:
            self.comendo = False
            print(f"{self.nome} parou de comendo")

    def dormir(self):
        if self.falando == False or self.andando == False or self.comer == False:
            self.dormindo = True
            print("ZzZzZzZz")
        elif self.falando == True:
            print(f"{self.nome} precisa parar de falar para dormir.")
        elif self.andando == True:
            print(f"{self.nome} precisa parar de andar para dormir.")

    def pararDormir(self):
        if self.dormindo == False:
            print(f"{self.nome} não está dormindo")
        else:
            self.dormindo = False
            print(f"{self.nome} parou de dormindo")

pessoa1 = pessoa("Ladilson", "17", "1.78", "62kg", "Masculino")