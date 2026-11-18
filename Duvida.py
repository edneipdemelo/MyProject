# Demonstração de match/case...
print("Devo ir ao baile?")
RESPOSTA = input()

match RESPOSTA:
    case "sim":
        print("Que bom! Estarei lá.")
    case "não":
        print("Pôxa, que pena!")
    case "talvez":
        print("Pensa direitinho...")
    case _:
        print("Já se decidiu?")

print("Será um baile e tanto!")