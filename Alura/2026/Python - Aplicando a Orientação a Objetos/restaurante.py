class Restaurante:
    restaurantes = []


    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

restaurante_praca = Restaurante('Sabor da Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza GOH', 'Italiana')

restaurantes = [restaurante_praca, restaurante_pizza]

print('Testes:')
print(f'Restaurante: {restaurante_praca.nome} - Categoria: {restaurante_praca.categoria} - Ativo: {restaurante_praca.ativo}')
print(f'Restaurante: {restaurante_pizza.nome} - Categoria: {restaurante_pizza.categoria} - Ativo: {restaurante_pizza.ativo}\n')

# __init__
print(vars(restaurante_praca))
print(vars(restaurante_pizza))

# __str__
print(restaurante_praca)
print(restaurante_pizza)

print('\nLista de restaurantes:')
Restaurante.listar_restaurantes()