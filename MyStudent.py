# Correção de exercícios...
NOTA1 = float(input("Digite a nota 1: "))
NOTA2 = float(input("Digite a nota 2: "))
NOTA3 = float(input("Digite a nota 3: "))
NOTA4 = float(input("Digite a nota 4: "))
MÉDIA = (NOTA1 + NOTA2 + NOTA3 + NOTA4) / 4

if MÉDIA >= 6:
    print("Você está aprovado!")
else:
    print("Você está reprovado...")

print(f"Sua média é {MÉDIA}.")
print(type(MÉDIA))