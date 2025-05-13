from PyQt5.QtWidgets import  QWidget, QMessageBox, QLineEdit, QPushButton,QWidget, QFormLayout, QLineEdit, QComboBox, QPushButton, QSpinBox
from TelaCategoria import CadastroCategoria
from Desktop import Desktop
from Categoria import Categoria

class CadastroDesktop(QWidget):
    def __init__(self, categorias):
        super().__init__()
        self.setWindowTitle("Cadastro de Desktop")
        self.setGeometry(150, 150, 400, 300)

        self.layout = QFormLayout()

        self.modelo_input = QLineEdit(self)
        self.cor_input = QLineEdit(self)
        self.preco_input = QLineEdit(self)
        self.categoria_input = QComboBox(self)
        self.categoria_input.addItems([categoria.nome for categoria in categorias])  # Exibir categorias disponíveis
        self.potencia_input = QSpinBox(self)
        self.potencia_input.setRange(100, 1000)

        self.cadastrar_button = QPushButton("Cadastrar", self)
        self.cadastrar_button.clicked.connect(self.cadastrarDesktop)

        
        self.layout.addRow("Modelo:", self.modelo_input)
        self.layout.addRow("Cor:", self.cor_input)
        self.layout.addRow("Preço:", self.preco_input)
        self.layout.addRow("Categoria:", self.categoria_input)
        self.layout.addRow("Potência da Fonte:", self.potencia_input)
        self.layout.addWidget(self.cadastrar_button)

        self.setLayout(self.layout)

    def cadastrarDesktop(self):
        modelo = self.modelo_input.text()
        cor = self.cor_input.text()
        preco = float(self.preco_input.text())
        categoria_nome = self.categoria_input.currentText()
        categoria = Categoria(id=1, nome=categoria_nome)

        potencia = self.potencia_input.value()

        if modelo and cor: 
            produto = Desktop(modelo, cor, preco, categoria, potencia)

            produto_info = produto.getInformacoes()

            QMessageBox.information(self, "Sucesso", "Desktop cadastrado com sucesso!\n\n" + produto_info)
            self.close()
        else:   
            print("Por favor, preencha todos os campos obrigatórios.")
