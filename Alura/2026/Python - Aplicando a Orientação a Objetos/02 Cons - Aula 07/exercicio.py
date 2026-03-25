#Em uma carreira de desenvolvimento de software, a prática consistente desempenha um papel fundamental na construção de bases sólidas. 
# Pensando nisso, criamos uma lista de atividades (não obrigatórias) focada em prática para melhorar ainda mais sua experiência de aprendizagem.
# Bora praticar então?
# Exercícios
# Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
# Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
# Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
# Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
# Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.

# Respostas
# 1) Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano.
#    Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

# Instanciando um carro e atribuindo valores aos seus atributos
meu_carro = Carro(modelo='Fusca', cor='Azul', ano=1970)



# 2) Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos.
#    Instancie um restaurante e atribua valores aos seus atributos.

class Restaurante:
    def __init__(self, nome, categoria, capacidade, nota_avaliacao, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao
        self.ativo = ativo

# Instanciando um restaurante e atribuindo valores aos seus atributos
restaurante_exemplo = Restaurante(
    nome='Comida Boa',
    categoria='Gourmet',
    capacidade=50,
    nota_avaliacao=4.5,
    ativo=True
)



# 3) Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros
#    e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.

class Restaurante:
    def __init__(self, nome, categoria, capacidade=0, nota_avaliacao=0.0, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao
        self.ativo = ativo

# Instanciando um restaurante utilizando o construtor
novo_restaurante = Restaurante(nome='Santa Marmita', categoria='Fast Food')



# 4) Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância,
#    seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.

class Restaurante:
    def __init__(self, nome, categoria, capacidade=0, nota_avaliacao=0.0, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao
        self.ativo = ativo

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

# Exibindo uma instância do restaurante formatada
restaurante_formatado = Restaurante(nome='Bom Sabor', categoria='Tradicional')
print(restaurante_formatado)



# 5) Crie uma classe chamada Cliente e pense em 4 atributos.
#    Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.

class Cliente:
    def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

# Instanciando três objetos da classe Cliente e atribuindo valores aos seus atributos através do construtor
cliente1 = Cliente(nome='Alice', idade=25, email='alice@gmail.com', telefone='123-456-7890')
cliente2 = Cliente(nome='Bob', idade=30, email='bob@gmail.com', telefone='987-654-3210')
cliente3 = Cliente(nome='Charlie', idade=22, email='charlie@gmail.com', telefone='555-123-4567')