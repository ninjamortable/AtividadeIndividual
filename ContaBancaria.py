from abc import ABC, abstractmethod
class ContaBancaria(ABC):
    def __init__(self, numeroConta, saldo):
        self.numeroConta = numeroConta
        self.saldo = saldo
    
    @abstractmethod
    def sacar(self):
        pass
    
    @abstractmethod
    def deposito(self):
        pass