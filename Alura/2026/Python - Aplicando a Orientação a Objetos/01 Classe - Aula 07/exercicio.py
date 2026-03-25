# Em uma carreira de desenvolvimento de software, a prática consistente desempenha um papel fundamental na construção de bases sólidas. 
# Pensando nisso, criamos uma lista de atividades (não obrigatórias) focada em prática para melhorar ainda mais sua experiência de aprendizagem. Bora praticar então?
#
#Exercícios
#Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
#Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
#Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
#Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
#Altere o valor do atributo nome para 'Bistrô'.
#Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
#Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
#Mude o estado da instância restaurante_pizza para ativo.
#Imprima no console o nome e a categoria da instância restaurante_praca. 

class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Sabor da Praça'
restaurante_praca.categoria = 'Italiana'
restaurante_praca.ativo

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
restaurante_pizza.ativo

nome_do_restaurante = restaurante_praca.nome

categoria = Restaurante.categoria

restaurante_praca.nome = 'Bistrô'

restaurante_pizza = Restaurante()

if restaurante_praca.ativo:
    print('O restaurante está ativo.')
else:
    print('O restaurante está inativo.')

if restaurante_pizza.categoria == 'Fast Food':
    print('A categoria é Fast Food.')
else:
    print('A categoria não é Fast Food.')

restaurante_pizza.ativo = True
    
print(f'Restaurante: {restaurante_praca.nome} | Categoria: {restaurante_praca.categoria} | Ativo: {restaurante_praca.ativo}')
print(f'Restaurante: {restaurante_pizza.nome} | Categoria: {restaurante_pizza.categoria} | Ativo: {restaurante_pizza.ativo}')