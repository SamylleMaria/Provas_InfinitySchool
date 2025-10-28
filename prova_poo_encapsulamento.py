"""Crie uma classe chamada ContaBancaria que tenha dois atributos privados, _saldo e _titular. O atributo _saldo deve armazenar o saldo da conta, enquanto o atributo _titular deve armazenar o nome do titular da conta. Para interagir com esses atributos, implemente métodos públicos que permitam realizar operações bancárias. Crie um método depositar que permita adicionar um valor ao saldo, um método sacar que permita retirar um valor do saldo (caso haja saldo suficiente), e um método exibir_saldo que exiba o saldo atual da conta. Utilize métodos para encapsular o acesso ao saldo, garantindo que ele só possa ser alterado de maneira controlada pelos métodos de depósito e saque."""


class ContaBancaria:   
    def __init__(self, titular: str, saldo: float):
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, valor: float):
        if valor > 0:
            self.__saldo += valor
            print(f"Deposito realizado, saldo atual: {self.__saldo}")
        else:
            print("Valor inválido")

    def sacar(self, valor: float):
        if self.__saldo >= valor:
            self.__saldo -= valor
            print(f"Saque realizado, saldo atual: {self.__saldo}")
        else:
            print("Saldo insuficiente")

    def exibir_saldo(self):
        print(f"Saldo atual: {self.__saldo}")

