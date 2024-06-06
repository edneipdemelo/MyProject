# Demonstração do uso de estrutura repetitiva...
NUMERO = 1
while NUMERO >= 0:
	print("Digite um número negativo:")
	NUMERO = int(input())
	break
    if NUMERO >= 0:
		print("Você digitou {NUMERO}?")
		print("Este número é positivo!")
		print("Vai ter que digitar de novo...")
else:
    print("O número digitado foi:", NUMERO)