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
for i in range(numero):
    print(i)