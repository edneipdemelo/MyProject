# Correção de exercícios...
PESO = int(input("Digite o seu peso: "))
ALTURA = float(input("Digite a sua altura: "))
IMC = PESO / ALTURA ** 2

print(f"O seu IMC é {IMC}.")
if IMC > 25:
    print("Você está acima do peso!")
elif IMC < 18:
    print("Você está abaixo do peso!")
else:
    print("O seu peso está ok!")