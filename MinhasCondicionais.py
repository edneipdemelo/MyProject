# Demonstração de Condicionais

Numero = int(input("Digite um valor: "))
if Numero == 0:
    print("Não pode digitar zero!")
elif Numero > 0 and Numero < 10:
    print("Ele é está entre zero e 10")
#else:
    print("Ele é qualquer outro valor!")

Nota = input("Digite a sua nota:")
match Nota:
    case "A":
        print("Excelente!")
    case "B":
        print("Boa!")
    case "C":
        print("Mais ou menos")
    case "D":
        print("Ruim")
    case "E":
        print("Péssima!")
    case _:
        print("Digitou errado!")