# Resolvendo o fatorial...
N = int(input("Digite o número: "))
FATORIAL = 1

if N < 1 or N > 25:
    print("Valor fora do intervalo!")
else:
    for X in range (1, N+1):
        FATORIAL = FATORIAL * X
    print(f"O fatorial de {N} é: {FATORIAL}")
