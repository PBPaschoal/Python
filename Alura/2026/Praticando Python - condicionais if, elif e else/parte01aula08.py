#Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. 
#Ele estabeleceu um limite de R$ 3.000,00 para seus gastos e precisa de um programa que ajude a controlar suas despesas. 
#O programa deve receber o total de despesas realizadas e informar se ele ultrapassou o limite ou ainda está dentro do orçamento.
#Saída esperada:
#Digite o total de despesas do mês (R$): 5897.58
#Atenção! Você ultrapassou o limite do orçamento.
despesas_entrada = float(input('Digite o total de despesas do mês (R$): '))
if despesas_entrada > 3000.00:
    print('Atenção! Você ultrapassou o limite do orçamento.')
else:
    print('Limite dentro do orçamento desejado.')

#Minha versão:
#Pergunte ao usuário o valor
#Depois pergunte se ele quer digitar outro valor
#se sim, ele informa o outro valor
#não o programa soma os valores (se houver para somar) e verifica se o(s) valor(es) digitado(s) é (são) maior(es) que 3 mil
#se sim: mensagem de atenção
#se não, tudo ok
print('\nMinha versão:')

total = 0

while True:
    despesas_entrada = float(input('Digite o total de despesas do mês (R$): '))
    total += despesas_entrada

    escolha = input('Deseja digitar outro valor (S/N)? ').upper()

    if escolha != 'S':
        break

if total > 3000:
    print('Atenção! Você ultrapassou o limite do orçamento.')
else:
    print(f'Limite dentro do orçamento desejado: R$ {total:.2f}')

print(f'Total de despesas: R$ {total:.2f}')