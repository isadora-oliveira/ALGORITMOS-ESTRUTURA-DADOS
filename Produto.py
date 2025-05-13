from abc import ABC, abstractmethod
from Categoria import Categoria


class Produto( ABC ):
    def __init__(self, modelo, cor, preco, categoria: Categoria):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.categoria = categoria

    @abstractmethod
    def getInformacoes(self):
        return f"{self.modelo}, {self.cor}, {self.preco}, {self.categoria.nome}"


    @abstractmethod
    def cadastrar(self):
        pass
