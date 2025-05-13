from Produto import Produto
from Notebook import Notebook
from Categoria import Categoria

class Desktop(Produto):
    def __init__(self, modelo, cor, preco, categoria, potenciaDaFonte):
        super().__init__(modelo, cor, preco, categoria)
        self._potencia = potenciaDaFonte

    def getInformacoes(self):
        return super().getInformacoes() + f", Potência: {self._potencia}W"

    def getPotenciaDaFonte(self):
        return self._potencia

    def setPotenciaDaFonte(self, potencia):
        self._potencia = potencia

    def cadastrar(self):
        return f"Desktop {self.modelo} cadastrado com sucesso!"

