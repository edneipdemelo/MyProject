# Correção de exercícios...
SEMANA = input("Digite o dia da semana: ")

match SEMANA:
    case "segunda":
        print("Dia de lavar roupa!")
    case "terça":
        print("Dia de varrer a casa!")
    case "quarta":
        print("Dia de cozinhar...")
    case "quinta":
        print("Dia de lavar o banheiro!")
    case "sexta":
        print("Sextou!!!")
    case "sábado":
        print("Churrasco na lage!")
    case "domingo":
        print("Devo ir à missa/culto?")
    case _:
        print("Não sei o que fazer...")