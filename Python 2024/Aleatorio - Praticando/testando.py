print("Ola")
print("Vamos praticar um pouco de Python")
resposta = 's'
if resposta == 's':
    print("Conseguiu!")
else:
    print("Nao conseguiu")

print("Vamos melhorar esse codigo?")

numero = int(input("Informe um número: "))

if numero < 10:
    print("O seu número é menor que 10!")
elif numero == 10:
    print("O seu número é igual a 10!")
else:
    print("O seu número é maior que 10!")

print("Vamos contar até ", numero)
for i in range(numero + 1):
    print(i)

idade = int(input("Informe a sua idade: "))

if idade < 18:
    print("Você é menor de idade e por isso não pode dirigir.")
else:
    print("Você já pode dirigir.\n")

digitar = int(input("\nQuantas vezes deseja digitar um número inteiro? "))

soma = 0
for i in range(digitar):
    numero_inteiro = int(input("Digite um numero: "))
    soma += numero_inteiro

print("A soma dos numeros digitados = ", soma)