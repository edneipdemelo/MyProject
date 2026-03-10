# Qual é o melhor time do Brasil?
TIME = ""
while True:
    TIME = input("Qual é melhor clube? ")
    if TIME != "América-RJ":
        print("Digitou errado!")
        print("Tente de novo...")
    else:
        print("Acertô, mizerávi!")
        break