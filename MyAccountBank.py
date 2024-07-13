# Demonstração de OOP em Python...
from abc import ABC, abstractmethod

class CLIENTE:
    @abstractmethod
    def __init__(self, TITULAR, CONTA, SALDO):
        self.TITULAR = TITULAR
        self.CONTA = CONTA
        self.SALDO = SALDO
    
    def APRESENTAR(self):
        print("Olá, eu sou a classe-pai!")
        pass

class CLIENTE_FISICO(CLIENTE):
    def APRESENTAR(self):
        print("Olá! Eu sou:", self.TITULAR)
        print("Minha conta é:", self.CONTA)
        print("E quero saber o meu saldo.")
        return

# Para criar uma instância baseada na classe CLIENTE...
FULANO = CLIENTE_FISICO("João", "423.050205-21", 25000.00)

# Executando o método da instância criada...
FULANO.APRESENTAR()

# Acessando os atributos das instâncias criadas...
print("De fato, você realmente é:", FULANO.TITULAR)
print("No momento, a sua conta possui R$", FULANO.SALDO)