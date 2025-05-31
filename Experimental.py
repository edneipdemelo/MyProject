import json
dados = {
    "Nome": "Fulano",
    "Idade": 20
}

json_strings = json.dumps(dados, indent=4)
conteudo = open("diario.txt", "w")
conteudo.write(json_strings)
conteudo.close()
