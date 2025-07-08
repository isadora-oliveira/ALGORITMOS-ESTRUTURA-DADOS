from Fabricante import Fabricante


class Veiculo:
    def __init__(self, marca:Fabricante, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.prox = None

    def __str__(self):
        txt = "Marca - Fabricante: " + self.marca.nome
        txt+= "\nMarca - Ano Fundação: " + str(self.marca.anoFundacao)
        txt += "\nModelo: " + self.modelo 
        txt += "\nAno: " + str(self.ano)
        return txt


        