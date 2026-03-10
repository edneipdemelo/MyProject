# Construa um programa onde o usuário digitará um valor e o programa mostrará, na tela, a tabuada de multiplicação desses números. Se possível, promova uma impressão que possibilite visualizar tais números da melhor maneira possível.
NUMERO = int(input("Digite o valor: "))
for X in range (1, 11):
    RESULTADO = X * NUMERO
    print(f"{X} x {NUMERO}:", RESULTADO)
