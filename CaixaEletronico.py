# Resolução do problema do caixa eletrônico...
SAQUE = int(input("Digite o valor: "))
CONT50 = 0; CONT20 = 0; CONT10 = 0

while True:
    if SAQUE >= 50:
        CONT50 += 1
        SAQUE = SAQUE - 50
    elif SAQUE >= 20:
        CONT20 += 1
        SAQUE = SAQUE - 20
    elif SAQUE >= 10:
        CONT10 += 1
        SAQUE = SAQUE - 10
    else:
        print("Valor abaixo do mínimo possível para sacar!")
        break

print(f"Irei receber {CONT50} notas de 50, {CONT20} notas de 20 e {CONT10} notas de 10.")
