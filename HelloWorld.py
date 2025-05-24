# Primeiro programa!

Nome = input("Digite o seu nome: ")
Idade = int(input("Digite a sua idade:"))
Conta = float(input("Digite o saldo da conta:"))

print()
print("Meu nome é", Nome, "a idade é", Idade, "e o valor da conta é", Conta)
print(f"Meu nome é {Nome}, a idade é {Idade} e o valor da conta é {Conta}")

print()
print(type(Nome))
print(type(Idade))
print(type(Conta))