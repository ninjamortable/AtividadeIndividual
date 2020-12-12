from ContaBancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def __init__(self, numeroConta, saldo, limite):
        super().__init__(numeroConta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print("Retirada Realizada com Sucesso")
            print(f"Novo saldo: {self.saldo}")
        elif (self.saldo + self.limite) <= valor:
            self.saldo -= valor
            print("Retirada Realizada com Sucesso")
            print(f"Novo saldo: {self.saldo}")
        else:
            print("Valor Maior que saldo")
            print(f"Saldo: {self.saldo}")

    def deposito(self, valor):
        self.saldo += valor
        print("Deposito Realizada com Sucesso")
        print(f"Novo saldo: {self.saldo}")
