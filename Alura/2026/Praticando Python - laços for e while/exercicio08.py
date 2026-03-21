#Ana está desenvolvendo seu portfólio para exibir os projetos de Python que concluiu. 
#Ela organizou uma lista com o nome de cada projeto, mas percebeu que alguns itens podem estar ausentes, aparecendo como None:
#projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]
#Crie um programa que ajude Ana a percorrer a lista de projetos e exiba os nomes dos projetos válidos. Se encontrar um item None, o programa deve exibir a mensagem: "Projeto ausente".
#Saída esperada:
#website
#jogo
#análise de dados
#Projeto ausente
#aplicativo móvel
projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for projeto in projetos:
    if projeto is None:
        print("Projeto ausente")
    else:
        print(projeto)