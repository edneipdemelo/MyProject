# Demonstração do uso de funções...
def ADICAO(X, Y):
    return X + Y
def SUBTRACAO(X, Y):
    return X - Y

print("Digite dois valores inteiros...")
N1 = int(input("X: "))
N2 = int(input("Y: "))
print("Qual operação deseja realizar?")
OP = input("Digite o símbolo do operador: ")

if OP == "+":
    Z = ADICAO(N1, N2)
    print("Resultado da soma:", Z)
elif OP == "-":
    Z = SUBTRACAO(N1, N2)
    print("Resultado da subtração:", Z)
else:
    print("Opção digitada inexistente!")