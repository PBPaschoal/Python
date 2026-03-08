#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
print('Todos os números pares que estão no intervalo entre 1 e 50:')
for i in range(1, 50):
    if i % 2 == 0:
        print(i)
print("FIM")