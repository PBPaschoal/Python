# -*- cding: utf-8 -*-

print("Qual o salario do professo?\n")

vh = float(input('Informe o valor hora aula: '))
ht = int(input('Informe o valor hora no mes:'))
pd = float(input('Informe o percentual do INSS '))

sb = vh * ht
td = (pd/100) * sb
sl = sb - td

print("\nSalario bruto: R$ ", sb)
print("Salario liquido: R$ ", sl)