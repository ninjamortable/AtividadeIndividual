from ContaPoupança import ContaPoupanca
from ContaCorrente import ContaCorrente

def main():
    conta = ContaPoupanca(231231, 2000, 200)
    conta.sacar(2200)
    conta.deposito(20000)

    print('-'*20)

    conta = ContaCorrente(231231, 2000, 0.10)
    #conta.sacar(2000)
    conta.deposito(20000)

main()