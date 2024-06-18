# Demonstração de acesso a listas...

MARMITA = ["feijão", "arroz", "legumes", "salada", "carne"]
print("Marmita com 5 alimentos!")
print("Eis, a nossa recomendação:", MARMITA)

for X in range(0, 5):
    print(f'Digite o {X+1}o. item do cardápio:')
    MARMITA[X] = input()

print("A marmita montada foi:", MARMITA)
print("O três primeiros itens foram:", MARMITA[0:3])
print("O último item da marmita foi:", MARMITA[-1])