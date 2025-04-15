import sys 
from PyQt5.QtWidgets import *

from TelaCategoria import TelaVeiculo
from TelaCarro import TelaCarro
from TelaCategoria import TelaCategoria

app = QApplication(sys.argv)

#TelaVeiculo
telaVeiculo = TelaVeiculo("Cadastro de Veículo")
telaVeiculo.show()

#TelaCategoria

categorias = []
telaCat = TelaCategoria("Cadastro de Categoria")

#TelaCarro
telaCarro = TelaCarro("Cadastro de Carro: ", categorias, telaCat)
telaCarro.show()

sys.exit(app.exec_())
