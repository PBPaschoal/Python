#Você está desenvolvendo um sistema de controle de estoque para o Buscante. 
#Um dos requisitos é verificar a quantidade de exemplares de um livro em estoque e continuar vendendo até que o estoque se esgote. 
#Sempre que uma venda é realizada, o sistema deve informar o usuário e atualizar a quantidade disponível.
#Crie um programa que simule as vendas de um livro com o estoque inicial de 5 exemplares. 
#O programa deve exibir a mensagem "Venda realizada! Estoque restante: <quantidade>" a cada venda e, ao final, exibir a mensagem "Estoque esgotado".
#Saída esperada:
#Venda realizada! Estoque restante: 4
#Venda realizada! Estoque restante: 3
#Venda realizada! Estoque restante: 2
#Venda realizada! Estoque restante: 1
#Venda realizada! Estoque restante: 0
#Estoque esgotado
estoque = 5
while estoque > 0:
    estoque -= 1
    print(f'Venda realizada! Estoque restante: {estoque}')

print('Estoque esgotado')