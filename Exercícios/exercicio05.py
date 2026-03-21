#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daquelas que forem pares. Se o valor digitado for ímpar, desconside-o.
contagem = 1
soma = 0
while contagem < 7:
    numero = int(input(f'{contagem}: Digite um valor: '))
    contagem += 1
    if numero % 2 == 0:
        soma += numero
print(f'Total: {soma}')