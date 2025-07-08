from Veiculo import Veiculo

class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None
    
    def add(self, veiculo:Veiculo):
        if self.inicio == None:
            self.inicio = veiculo
        elif self.inicio.prox is None:
            self.inicio.prox = veiculo
        else:
            aux = self.inicio
            while aux.prox:
                aux = aux.prox
            aux.prox = veiculo
            self.fim = veiculo
            self.imprimir()
            

    def imprimir(self):
        print( "-------------------------------")
        if self.inicio == None:
            print( "Lista de veículos está vazia!")
        else:
            aux = self.inicio
            txt = ""
            while aux != None:
                txt += str(aux) + "\n"
                txt += "-------------------------------\n"
                aux = aux.prox
            print(txt)

    def excluir(self):
        print( "Veiculo " + self.inicio.modelo + " removido!")
        if self.inicio is not None:
            self.inicio = self.inicio.prox
            if self.inicio == None:
                self.fim = None


