from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QSpinBox, QComboBox, QPushButton, QMessageBox
from Notebook import Notebook
from Categoria import Categoria

class CadastroNotebook(QWidget):
    def __init__(self, categorias):
        super().__init__()
        self.setWindowTitle("Cadastro de Notebook")
        self.setGeometry(100, 100, 400, 300)
        self.categorias = categorias

    
        self.layout = QFormLayout()

        self.modelo_input = QLineEdit(self)
        self.cor_input = QLineEdit(self)
        self.preco_input = QLineEdit(self)
        self.categoria_input = QComboBox(self)
        self.categoria_input.addItems([categoria.nome for categoria in categorias])
        self.bateria_input = QSpinBox(self)
        self.bateria_input.setRange(1, 24)

      
        self.layout.addRow("Modelo:", self.modelo_input)
        self.layout.addRow("Cor:", self.cor_input)
        self.layout.addRow("Preço:", self.preco_input)
        self.layout.addRow("Categoria:", self.categoria_input)
        self.layout.addRow("Tempo de Bateria:", self.bateria_input)

     
        self.cadastrar_button = QPushButton("Cadastrar", self)
        self.cadastrar_button.clicked.connect(self.cadastrarNotebook) 
        self.layout.addWidget(self.cadastrar_button)

        self.setLayout(self.layout)

    def cadastrarNotebook(self):
    
        modelo = self.modelo_input.text()
        cor = self.cor_input.text()
        preco = float(self.preco_input.text())
        tempo_bateria = self.bateria_input.value()
        categoria_nome = self.categoria_input.currentText()
        categoria = next((c for c in self.categorias if c.nome == categoria_nome), Categoria(0, "Desconhecida"))

        notebook = Notebook(modelo, cor, preco, categoria, tempo_bateria)
        info = notebook.getInformacoes()

        QMessageBox.information(self, "Sucesso", "Notebook cadastrado com sucesso!\n\n" + info)
        self.close()