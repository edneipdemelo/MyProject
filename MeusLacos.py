# Quero contar até...

Numero = int(input("Digite até quanto: "))
for Contador in range(0, Numero + 1):
    print("Número", Contador)

Numero = int(input("Digite até quanto: "))
Contador = 0
while Contador <= Numero:
    print("Número", Contador)
    Contador = Contador + 1

Nomes = ["Fulano", "Beltrano", "Ciclano"]
for Pessoas in Nomes:
    print("Olá", Pessoas)