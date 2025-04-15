import sys 
from PyQt5.QtWidgets import *
from TelaCategoria import TelaVeiculo
from Categoria import Carro


class TelaCarro (TelaVeiculo):
    def __init__(self, titulo="Tela Carro", categorias = [], telaCat = None):
        self.telaCategoria = telaCat
        self.listaCategorias = categorias
        super().__init__(titulo) #função super() afirma que o init da superclasse será a mesma da declarada de quem ela herda. Neste caso, a classe TelaCarro recebe os mesmos parâmateros e funções de TelaVeiculo
        self.setGeometry(450, 150, 300, 300)

    def definirLayout(self): # estou redefinindo uma função que já existe e herdei de TelaVeiculo,o nome disto é POLIMORFISMO: o ato de alterar funções de classes herdadas, mas mantendo outras comooriginalmente são.
        super().definirLayout()
        self.lblPortas = QLabel("Quantidade de portas: ")
        self.txtPortas = QLineEdit(self) #QLineEdit recebe somente o que a própria classe recebe, por isto self
        self.layout.addWidget(self.lblPortas)
        self.layout.addWidget(self.txtPortas)

        self.lblCategoria = QLabel("Categoria")
        self.layout.addWidget(self.lblCategoria)

        self.cmbCategoria = QComboBox(self)
        self.carregarCategorias()
        self.layout.addWidget(self.cmbCategoria)

        self.btnAbrirTelaCat = QPushButton("Add Categoria", self)
        self.btnAbrirTelaCat.clicked.connect(self.abrirTelaCategoria)
        self.layout.addWidget(self.btnAbrirTelaCat)

    def abrirTelaCategoria(self):
        self.telaCategoria.show()

    def carregarCategorias(self):
        self.cmbCategoria.addItem("Selecione...", None)
        for cat in self.listaCategorias:
            self.cmbCategoria.addItem(cat.nome, cat)


    def salvar(self):
        modelo = self.txtModelo.text() #modelo recebeu o QLineEdit, que é classe contendo um texto com as dimensões, com o final .text() eu estou afirmando que esta variável recebe somente a parte de texto da classe QLineEdit.
        ano = self.txtAno.text() #mesma lógica.
        if(ano != ""): #se o ano não for vazio,
            ano = int(ano) #variável ano recebe o ano como um número inteiro,
        portas = self.txtPortas.text()
        if portas != "":
            portas = int(portas)
        carro = Carro(modelo, ano, portas) #variável carro recebe a classe Carro com as variáveis definidas na função (modelo, ano, portas) que são os parâsmetros que ela normalmente recebe.
        QMessageBox.information(self, "Carro salvo", str(carro) )