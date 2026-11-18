print("Qual o seu saldo atual?")
Saldo = int(input())
print("Qual o valor do item que deseja comprar?")
Compra = int(input())

Total = Saldo - Compra
print(Total)

if Total >= 0:
    print("Você não pode realizar essa compra.")
else:
    print("Você pode realizar essa compra.")