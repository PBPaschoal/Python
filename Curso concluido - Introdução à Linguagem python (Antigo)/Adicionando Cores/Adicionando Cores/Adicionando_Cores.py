#Dia 09 de Maior de 2021 às 18:03hrs
#Curso Python Aula 11 Cores no Terminal

print('\033[0;33;44mOlá, Mundo!\033[m')
a = 3
b = 5
print('Os valores são \033[32;44m{}\033[m e \033[1;44{}\033[m!!!'.format(a, b))
nome = 'Paulo'
print('Olá! Muito prazer em teconhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format(cores['pretoebranco'], nome, cores['limpa']))
