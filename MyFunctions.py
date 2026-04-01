# Demonstração de funções...

def APRESENTAR():
    print(f"Meu nome é {MyName}.")
    print(f"Minha altura é {MyHeight}.")
    print(f"Minha idade é {MyAge}.")

def CONFERIR(X):
    if X >= 18:
        print("Você é maior de idade!")
    else:
        print("Você é menor de idade!")

MyName = input("Digite o seu nome: ")
MyHeight = float(input("Digite a sua altura: "))
MyAge = int(input("Digite a sua idade: "))

APRESENTAR()
CONFERIR(MyAge)