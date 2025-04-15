import sys 
from PyQt5.QtWidgets import *
from Categoria import Categoria
from TelaCarro import TelaCarro

class TelaCategoria(QMainWindow):

    def __init__(self, titulo = "Tela Categoria", categorias=[], telaCarro = None):
        self.listaCategorias = categorias
        self.telaCarro = telaCarro
        super().__init__()

        self.setWindowTitle(titulo)
        self.setGeometry(100, 150, 200, 150) #setGeometry(x, y, largura, altura)
        self.layout = QVBoxLayout()

        self.definirLayout()
        #botão
        self.btnSalvar = QPushButton("Salvar", self) 
        self.btnSalvar.clicked.connect(self.__salvar)
        self.layout.addWidget(self.btnSalvar)

        container = QWidget() #Criei um container com a classe QWdiget
        container.setLayout(self.layout) #setei o layout
        self.setCentralWidget(container) #Defini que este widget é central
    
    def definirLayout(self):
        self.lblNome = QLabel("Modelo: ")
        self.txtNome = QLineEdit(self)
        self.layout.addWidget(self.lblNome) 
        self.layout.addWidget(self.txtNome)
    
    
    #implementar o botão salvar
    def __salvar(self):
        nome = self.txtNome.text()
       
        if(nome != ""): #se o ano não for vazio,
            cat = Categoria(nome)
            self.listaCategorias.append(cat)    
            self.telaCarro.carregarCategorias()
        QMessageBox.information(self, "Categoria salva", str(cat) )
