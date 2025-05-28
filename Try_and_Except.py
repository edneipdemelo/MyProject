# Demonstração de tratamento de erros (exceções)

a = int(input("Digite o dividendo: "))
b = int(input("Digite o divisor: "))

try:
    result = a / b
except ZeroDivisionError:
    print("Você não pode realizar a divisão por zero!")
else:
    print(f"O resultado de {a} dividido por {b} é: {result}!")
finally:
    print("Isto será exibido, não importa o que aconteça!")