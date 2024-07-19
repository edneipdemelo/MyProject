# Correção de atividades...
X = int(input("Digite o valor de X: "))
Y = int(input("Digite o valor de Y: "))
Z = int(input("Digite o valor de Z: "))

if X < Y and Y < Z:
    print("Estão em ordem crescente!")
elif X > Y and Y > Z:
    print("Estão em ordem decrescente!")
else:
    print("Estão misturados...")