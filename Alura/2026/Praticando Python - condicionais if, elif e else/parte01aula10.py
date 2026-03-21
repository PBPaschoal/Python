#Uma professora precisa de um programa que ajude a calcular a média final dos alunos e informe se foram aprovados, ficaram de recuperação ou reprovados. As regras são:
#Média >= 7: Aprovado
#5 <= Média < 7: Recuperação
#Média < 5: Reprovado
#Escreva um programa que receba três notas como entrada e calcule a média final. Com base na média, exiba a situação do aluno.
#Saída esperada:
#Digite a primeira nota: 5.3
#Digite a segunda nota: 6.7
#Digite a terceira nota: 8.3
#Média: 6.77
#Recuperação
primeira_nota = float(input('Digite a primeira nota: '))
segunda_nota = float(input('Digite a segunda nota: '))
terceira_nota = float(input('Digite a terceira nota: '))
media = (primeira_nota + segunda_nota + terceira_nota) / 3.0
print(f'Média: {media:.2f}')
if media >= 7:
    print('Aprovado')
elif 5 <= media < 7:
    print('Recuperação')
else:
    print('Reprovado')