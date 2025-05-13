from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QComboBox, QSpinBox, QPushButton, QLabel, QFormLayout
from Categoria import Categoria
from TelaDesktop import CadastroDesktop
from TelaNotebook import CadastroNotebook
from TelaCategoria import CadastroCategoria


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu de Cadastro")
        self.setGeometry(100, 100, 300, 150)

        self.categorias = []
        
        layout = QVBoxLayout()

        btn1 = QPushButton("Cadastrar Desktop")
        btn1.clicked.connect(self.abrirDesktop)
        layout.addWidget(btn1)

        btn2 = QPushButton("Cadastrar Notebook")
        btn2.clicked.connect(self.abrirNotebook)
        layout.addWidget(btn2)

        btn3 = QPushButton("Cadastrar Categoria")
        btn3.clicked.connect(self.abrirCategoria)
        layout.addWidget(btn3)

        self.setLayout(layout)

    def abrirDesktop(self):
        self.win = CadastroDesktop(self.categorias)
        self.win.show()

    def abrirNotebook(self):
        self.win = CadastroNotebook(self.categorias)
        self.win.show()

    def abrirCategoria(self):
        # Agora, a função callback é passada para a tela de categoria
        self.win = CadastroCategoria(self.categorias, self.atualizarCategorias)
        self.win.show()

    def atualizarCategorias(self):
        # Atualiza as categorias nas telas de cadastro
        print("Categorias atualizadas:", [categoria.nome for categoria in self.categorias])

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())