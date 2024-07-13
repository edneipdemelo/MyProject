# Demonstração do uso de estrutura repetitiva...
NUMERO = 1
while NUMERO >= 0:
    print("Digite um número negativo para sair:")
    NUMERO = int(input())
    break
    print("Este texto não será exibido! Mas...")
else:
    print("O número digitado foi:", NUMERO)