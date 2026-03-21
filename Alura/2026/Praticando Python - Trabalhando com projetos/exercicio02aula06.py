#Carlos trabalha em um cartório e precisa validar se um CPF informado pelo cliente tem o formato correto antes de prosseguir com o atendimento. 
#O CPF deve conter exatamente 11 dígitos numéricos. Se a entrada contiver letras ou qualquer outro caractere que não seja um número, o programa deve exibir uma mensagem de erro.
#
#Crie um programa que peça ao usuário um número de CPF e verifique se ele tem 11 dígitos e contém apenas números.
#
#Exemplo de entrada:
#
#Digite seu CPF: 12345678901
#
#Saída esperada:
#
#CPF válido.
#
#Se for inválido:
#
#Digite seu CPF: 1234abc567  
#Erro: O CPF deve conter apenas números.  
#
#Se o CPF tiver um número de dígitos diferente de 11:
#
#Digite seu CPF: 1234567  
#Erro: O CPF deve ter exatamente 11 dígitos.  

try:
    numero_cpf = int(input('Digite seu CPF: '))
    if len(str(numero_cpf)) == 11:
        print('CPF válido.')
    else:
        print('Erro: O CPF deve ter exatamente 11 dígitos.')
except ValueError:
    print('Erro: O CPF deve conter apenas números.')

#Ou podemos fazer assim também:
#def validar_cpf(cpf):
#    if not cpf.isdigit():
#        return "Erro: O CPF deve conter apenas números."
#    if len(cpf) != 11:
#        return "Erro: O CPF deve ter exatamente 11 dígitos."
#    return "CPF válido."
# 
#cpf = input("Digite seu CPF: ")
#print(validar_cpf(cpf))