# Correção de atividades.
NOTA1 = int(input("Digite a primeira nota: "))
NOTA2 = int(input("Digite a segunda nota: "))
MEDIA = (NOTA1 + NOTA2) / 2

if MEDIA >= 6:
    print("Aprovado!")
elif MEDIA >= 4 and MEDIA < 6:
    NOTA3 = int(input("Digite a nota da recuperaçao: "))
    if NOTA3 >= 5:
        print("Aprovado na recuperação!")
    if NOTA3 < 5:
        print("Reprovado na recuperação")
else:
    print("Estudante reprovado!")