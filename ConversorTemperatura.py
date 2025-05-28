# Este programa irá realizar a conversão de temperaturas...

print("Conversão de temperaturas!")
print("Qual sistema de medição a usar:")
print("1. Celsim / 2. Kelvin / 3. Fahrenheit")
S = int(input("Digite a opção: "))
T = float(input("Digite o valor da temperatura: "))

if S == 1:
    F = 1.8 * T + 32
    K = T + 273.15
    print("A temperatura em Fahrenheit: ", F)
    print("A temperatura em Kelvin: ", K)
elif S == 2:
    C = T - 273.15
    F = (9/5 * (T - 273)) + 32
    print("A temperatura em Celsium: ", C)
    print("A temperatura em Fahenreit: ", F)
elif S == 3:
    C = (T - 32) / 1.8
    K = (273 + (5/9) * (T - 32))
    print("A temperatura em Celsim: ", C)
    print("A temperatura em Kelvin: ", K)
else:
    print("Opção inválida!")