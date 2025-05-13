from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton
from Categoria import Categoria

class CadastroCategoria(QWidget):
    def __init__(self, categorias, callback=None):
        super().__init__()
        self.setWindowTitle("Cadastro de Categoria")
        self.setGeometry(150, 150, 300, 150)
        self.layout = QVBoxLayout()

        self.nome_input = QLineEdit(self)
        self.layout.addWidget(self.nome_input)

        self.cadastrar_button = QPushButton("Cadastrar Categoria", self)
        self.cadastrar_button.clicked.connect(self.cadastrarCategoria)
        self.layout.addWidget(self.cadastrar_button)

        self.categorias = categorias
        self.callback = callback  # O callback pode ser None se não for passado
        self.setLayout(self.layout)

    def cadastrarCategoria(self):
        nome_categoria = self.nome_input.text()
        if nome_categoria:
            nova_categoria = Categoria(len(self.categorias) + 1, nome_categoria)
            self.categorias.append(nova_categoria)
            if self.callback:  # Verifica se o callback foi passado
                self.callback()  # Atualiza a lista de categorias nas telas de cadastro
            self.close()