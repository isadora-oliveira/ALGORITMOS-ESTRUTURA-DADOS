from Produto import Produto

class Notebook(Produto):
    def __init__(self, modelo, cor, preco, categoria, tempoDeBateria):
        super().__init__(modelo, cor, preco, categoria)
        self.__tempoDeBateria = tempoDeBateria

    def getInformacoes(self):
         return super().getInformacoes() + f", Bateria: {self.__tempoDeBateria}h"

    def getTempoBateria(self):
        return self.__tempoDeBateria

    def setTempoBateria(self, tempoDeBateria):
        if tempoDeBateria > 0:
            self.__tempoDeBateria = tempoDeBateria

    def cadastrar(self):
        return f"Notebook {self.modelo} cadastrado com sucesso!"
