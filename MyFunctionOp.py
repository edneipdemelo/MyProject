# Demonstração do uso de funções...
def ADICAO(X, Y):
    W = X + Y
    return W
def SUBTRACAO(X, Y):
    return X - Y
def MULTIPLICACAO(X, Y):
    return X * Y
def DIVISAO(X, Y):
    return X / Y

print("Digite dois valores inteiros...")
N1 = int(input("X: "))
N2 = int(input("Y: "))
OP = input("Qual operação (+, -, * ou /)?")

if OP == "+":
    Z = ADICAO(N1, N2)
    print("Resultado da soma:", Z)
elif OP == "-":
    Z = SUBTRACAO(N1, N2)
    print("Resultado da subtração:", Z)
elif OP == "*":
    Z = MULTIPLICACAO(N1, N2)
    print("O resultado da multiplicação:", Z)
elif OP == "/":
    Z = DIVISAO(N1, N2)
    print("O resultado da divisão:", Z)
else:
    print("Opção digitada inexistente!")