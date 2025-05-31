# Gerenciando as minhas séries favoritas...
Series = []
Servicos = []
Temporadas = []
Opcao = 1

while Opcao != 0:
    print("=/ Menu /=")
    print("1. Exibir / 2. Cadastrar / 3. Alterar / 4. Excluir")
    Opcao = int(input("Digite 0 para sair: "))

    match Opcao:
        case 1:
            if Series == []:
                print("Não há dados cadastrados!")
            else:
                for X in (range(0, len(Series))):
                    print("Série: ", Series[X], "Serviço: ", Servicos[X], "Temporada: ", Temporadas[X])
        case 2:
            Serie = input("Digite a série: ")
            Servico = input("Digite o serviço: ")
            Temporada = input("Digite a temporada: ")
            Series.append(Serie)
            Servicos.append(Servico)
            Temporadas.append(Temporada)
            print(f"Série {Serie} cadastrada com sucesso!")
        case 3:
            nome = input("Digite o nome da série para atualizar: ")
            if nome in Series:
                idx = Series.index(nome)
                nova_temp = int(input(f"Digite a nova temporada assistida de '{nome}': "))
                Temporadas[idx] = nova_temp
                print(f"Temporada da série '{nome}' atualizada com sucesso!")
            else:
                print("Série não encontrada.")
        case 4:
            if Series == []:
                print("Não há dados cadastrados!")
            else:
                Serie = input("Digite a série que deseja remover: ")
                for Z in (range(0, len(Series))):
                    if Serie == Series[Z]:
                        del(Series[Z])
                        del(Servicos[Z])
                        del(Temporadas[Z])
