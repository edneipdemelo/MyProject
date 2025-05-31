# Este programa irá realizar a conversão de temperaturas...

def Celsium_Kelvin(K):
    K = T + 273.15
    print("A temperatura em Kelvin: ", K)
def Celsium_Farenheit(F):
    F = 1.8 * T + 32
    print("A temperatura em Fahrenheit: ", F)
def Kelvin_Celsium(C):
    C = T - 273.15
    print("A temperatura em Celsium: ", C)
def Kelvin_Farenheit(F):
    F = (9/5 * (T - 273)) + 32
    print("A temperatura em Fahenreit: ", F)
def Farenheit_Celsim(C):
    C = (T - 32) / 1.8
    print("A temperatura em Celsim: ", C)
def Farenheit_Kelvin(K):
    K = (273 + (5/9) * (T - 32))
    print("A temperatura em Kelvin: ", K)

print("Conversão de temperaturas!")
print("Qual sistema de medição a usar:")
print("1. Celsim / 2. Kelvin / 3. Fahrenheit")

S = 0
T = 0
try:
    S = int(input("Digite a opção: "))
    T = float(input("Digite o valor da temperatura: "))
except:
    print("Não foram digitados valores numéricos!")
else:
    if S == 1:
        if T <= -273:
            print("Não pode valor abaixo do zero absoluto!")
        else:
            Celsium_Kelvin(T)
            Celsium_Farenheit(T)
    elif S == 2:
        if T <= 0:
            print("Não pode valor abaixo do zero absoluto!")
        else:
            Kelvin_Celsium(T)
            Kelvin_Farenheit(T)
    elif S == 3:
        if T <= -459:
            print("Não pode valor abaixo do zero absoluto!")
        else:
            Farenheit_Celsim(T)
            Farenheit_Kelvin(T)
    else:
        print("Opção inválida!")
