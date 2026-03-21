#Pedro quer solicitar um empréstimo, mas a aprovação depende de duas condições:
#O valor da renda mensal precisa ser maior que R$ 2.000,00.
#O valor da parcela não pode ultrapassar 30% da renda.
#Crie um programa que receba como entrada a renda mensal de Pedro e o valor da parcela desejada. 
#O programa deve informar se o empréstimo foi aprovado ou negado com base nas condições acima.
#Saída esperada:
#Digite o valor da sua renda mensal: 2500
#Digite o valor da parcela desejada: 800
#Empréstimo negado: parcela acima de 30% da renda.
valor_renda_mensal = float(input('Digite o valor da sua renda mensal: '))
valor_parcela_desejada = float(input('Digite o valor da parcela desejada: '))
parcela_maxima = valor_renda_mensal * 0.30
if valor_renda_mensal < 2000:
    print('Empréstimo negado: Renda mensal menor que o permitido.')
elif valor_parcela_desejada > parcela_maxima:
    print('Empréstimo negado: parcela acima de 30% da renda.')
else:
    print('Empréstimo aprovado.')