# Correção de atividade...
SEXO = input("Digite o sexo (M/F):" )
IDADE = int(input("Digite a idade:"))
TEMPO = int(input("Digite o tempo de contribuição: "))
INSALUBRE = input("Foi exposto a condições insalubres?")

if INSALUBRE == "sim":
    TEMPO == TEMPO * 1.4

if SEXO == "M" and IDADE >= 65 and TEMPO >= 35:
    print("Você está pronto para se aposentar!")
elif SEXO == "F" and IDADE >= 62 and TEMPO >= 30:
    print("Você está pronta para se aposentar!")
else:
    print("Sinto-lhe dizer, mas não poderá se aposentar...")
