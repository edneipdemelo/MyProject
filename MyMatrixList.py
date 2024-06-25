# Demonstração de matrizes em Python...
TABUADA = []

for X in range (0, 10):
    LINHAS = []
    for Y in range (0, 10):
        LINHAS.append(X * Y)
    TABUADA.append(LINHAS)

for TABELA in TABUADA:
    print(TABELA)