# Demonstração do uso de funções...
def APRESENTAR():
    print("Meu nome é", MyName, ".")
    print("Minha altura é de", MyHeigh, "metros")
    print("Minha idade é", MyAge, "anos.")
    return
def CONFERIR(X):
    if X >= 18:
        print("Você é maior de idade!")
    else:
        print("Ops, menor de idade não pode!")
    return

MyName = str(input("Digite o seu nome: "))
MyHeigh = float(input("Digite a sua altura: "))
MyAge = int(input("Digite a sua idade: "))

APRESENTAR()
CONFERIR(MyAge)