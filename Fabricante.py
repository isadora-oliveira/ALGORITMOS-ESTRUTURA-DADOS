class Fabricante:
    def __init__(self, nome, anoFundacao):
        self.nome = nome
        self.anoFundacao = anoFundacao

    def __str__(self):
        txt = "Nome: " + self.nome 
        txt += "\nAno Fundação: " + self.anoFundacao 
        return txt