nome = input("Digite seu nome: ")
print(f"Olá, {nome}! Bem-vindo ao nosso programa.")

idade = int(input("Digite sua idade: "))
print(f"Você tem {idade} anos.")

altura = float(input("Digite sua altura em metros: "))
print(f"Sua altura é {altura} metros.")

inicial = input("Digite a inicial do seu nome: ")
print(f"A inicial do seu nome é {inicial}.")

resposta = input("Você gosta de programar? (sim/não): ").lower()
gosta_de_programar = resposta == 'sim'
print(f"Você gosta de programar: {gosta_de_programar}")
