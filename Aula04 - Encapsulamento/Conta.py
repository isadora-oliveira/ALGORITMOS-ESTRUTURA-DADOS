class Conta: 
    logado = True

    def __init__(self):
        self.__saldo = 0.0
        self.tarifa = 1.99

    def getSaldo(self):
        if self.logado:
            return self.__saldo
        else: 
            return None
    
    def setSaldo(self, valor):
        if valor > self.__saldo:
            self.__saldo = valor 

    def __descontarTarifa(self):
        self.__saldo -= self.tarifa 

    def sacar(self, valor):
        if self.__saldo >= self.valor + self.tarifa:
            self.__saldo -= valor
            self.__descontarTarifa()
            print("Saque realizado com sucesso! :)")
        else:
            print("Saldo Insuficiente! :(")

    
#Property

    @property
    def saldo(self):
        if self.logado:
            return self.__saldo
        else:
            return None
        
    @saldo.setter
    def saldo(self, valor):
        if valor > self.__saldo:
            self.__saldo = valor

x = Conta()
x.setSaldo(1000)
print(x.getSaldo())

y = Conta()
y.saldo = 100
print(y.saldo)