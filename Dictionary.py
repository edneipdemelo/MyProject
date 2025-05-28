# Demonstração de uso de dicionários...

MyDict = {"Nome":"Fulano", "Função":"Administrador",
          "Salário":10000, "Avaliação":10}
# print("O meu salário é", MyDict["Salário"])

for Chave, Valor in MyDict.items():
    print("A chave é:", Chave)
    print("O valor é:", Valor)
    print()
