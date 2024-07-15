# Cadastro das informações...
print("Digite o nome da empresa:")
MyCompany = input()
print("Digite o nome do gestor:")
MyManager = input()
print("Digite o seu cargo:")
MyJob = input()
print("Data de início do aviso prévio:")
DataInicio = input()
print("Data do fim do aviso prévio:")
DataFim = input()

# Impressão da carta de demissão...
print(f"À {MyCompany},")
print(f"Prezado(a) {MyManager},")
print(f"Venho por meio desta carta comunicar formalmente o meu pedido de demissão do cargo de {MyJob}")
print(f"Estarei a disposição da empresa durante o aviso prévio, no período de {DataInicio} a {DataFim}.")
