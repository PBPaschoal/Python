# No Python, a criação de classes é uma parte essencial da programação orientada a objetos. 
# Abaixo, temos um exemplo de uma classe chamada Musica que representa informações sobre uma música, como nome, artista e duração:
#
#class Musica:
#    nome = ''
#    artista = ''
#    duracao = int
# Agora é sua vez! Refaça essa classe Musica utilizando uma forma mais concisa e expressiva, aproveitando a sintaxe simplificada do Python.

class Musica:
    def __init__(self, nome='', artista='', duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

musica1 = Musica(nome='Under Pressure', artista='Queen & David Bowie', duracao=248)
musica2 = Musica(nome='The Trooper', artista='Iron Maiden', duracao=245)
musica3 = Musica(nome='Hotel California', artista='Eagles', duracao=390)