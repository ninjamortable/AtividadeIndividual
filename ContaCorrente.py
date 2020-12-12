from ContaBancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self, numeroConta, saldo, taxa):
        super().__init__(numeroConta, saldo)
        self.taxa = taxa

    def sacar(self, valor):
        if self.saldo >= valor+(valor*self.taxa/100):
            self.saldo -= valor+(valor*self.taxa/100)
            print("Retirada Realizada com Sucesso")
            print(f"Novo saldo: {self.saldo}")

        else:
            print("Valor Maior que saldo")
            print(f"Saldo: {self.saldo}")



    def deposito(self, valor):
        self.saldo += valor-(valor*self.taxa/100)
        print("Deposito Realizada com Sucesso")
        print(f"Novo saldo: {self.saldo}")