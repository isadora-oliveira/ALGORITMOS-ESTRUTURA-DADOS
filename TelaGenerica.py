from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QComboBox, QPushButton

class TelaGenerica(QWidget):
    def __init__(self, categorias):
        super().__init__()
        self.setGeometry(100, 100, 400, 300)
        self.layout = QFormLayout()
        self.setLayout(self.layout)
        self.camposGenericos()
        self.categorias = categorias

    def camposGenericos(self):
        self.modelo_input = QLineEdit(self)
        self.cor_input = QLineEdit(self)
        self.preco_input = QLineEdit(self)
        self.categoria_input = QComboBox(self)
        self.categoria_input.addItems([categoria.nome for categoria in self.categorias])

        self.layout.addRow("Modelo:", self.modelo_input)
        self.layout.addRow("Cor:", self.cor_input)
        self.layout.addRow("Preço:", self.preco_input)
        self.layout.addRow("Categoria:", self.categoria_input)