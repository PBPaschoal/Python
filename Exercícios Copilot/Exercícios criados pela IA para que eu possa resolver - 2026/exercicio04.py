# Do básico ao avançado!
# Exercício 04
# - Calcular a média de três notas
# - Some as notas e divida por 3.
# - Dica: pense em como mostrar se o aluno está aprovado (média ≥ 7).

# Primeira versão
primeiraNota = float(input('Digite a primeira nota: '))
segundaNota = float(input('Digite a segunda nota: '))
terceiraNota = float(input('Digite a terceira nota: '))
media = (primeiraNota + segundaNota + terceiraNota) / 3.0
if media >= 7.0:
    print(f'Sua media é {media:.2f} e você está aprovado!')
elif media >= 5.0:
    print(f'Sua media é {media:.2f} e você está em recuperação!')
else:
    print(f'Sua media é {media:.2f} e você está reprovado!')
