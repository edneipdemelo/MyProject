# Correção de exercícios...
POSICAO = input("Digite a posição que você joga: ")

if POSICAO == "goleiro" or POSICAO == "zagueiro" or POSICAO == "lateral":
    print("Você joga na defesa!")
elif POSICAO == "volante" or POSICAO == "meia":
    print("Você joga no meio-campo!")
elif POSICAO == "ponta" or POSICAO == "atacante" or POSICAO == "centroavante":
    print("Você joga no ataque!")
else:
    print("Você joga de teimoso...")