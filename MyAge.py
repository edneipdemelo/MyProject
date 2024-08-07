# Demonstração do uso de funções
def MENOR():
    print("Eis, os programas ideais para você:")
    print("Teletubies, Tom & Jerri, Xou da Xuxa...")
    print("Se passar das 10h, vai dormir!!!")
    return
def MAIOR():
    print("Eis, boas opções de carro para comprar:")
    print("Fiat 147, VW Fusca, Chevette...")
    print("Se beber, não dirija...")
    return

print("Digite a sua idade:")
IDADE = int(input())

if IDADE < 18:
    MENOR()
else:
    MAIOR()