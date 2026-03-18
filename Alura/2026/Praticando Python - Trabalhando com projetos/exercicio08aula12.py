#Carlos está criando uma calculadora simples, mas quer garantir que o programa não quebre se o usuário digitar valores inválidos, ele precisa tratar os erros.
#
#Crie uma calculadora que permita ao usuário escolher entre soma, subtração, multiplicação e divisão. 
#Além de modularizar o código em funções, use try-except para tratar erros de entrada inválida, que consiste em:
#
#Caso digite um caractere em vez de número | exceção a ser lançada: ValueError;
#Caso tente fazer uma divisão por 0 | exceção a ser lançada: ZeroDivisionError.
#Exemplo de entrada:
#
#Digite o primeiro número: 5
#Escolha a operação (+, -, *, /): +
#Digite o segundo número: 7
#
#Saída esperada:
#
#Resultado: 12
#
#Caso selecione nenhuma das operações listadas:
#
#Opção inválida
#
#Caso digite um caractere em vez de número:
#
#Erro: Entrada inválida. Digite apenas números.
#
#Caso tente fazer uma divisão por 0:
#
#Erro: Divisão por zero não é permitida.

def somar(num1, num2):
    return num1 + num2
 
def subtrair(num1, num2):
    return num1 - num2
 
def multiplicar(num1, num2):
    return num1 * num2
 
def dividir(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError
    return num1 / num2
 
def calculadora():
    try:
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Escolha a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))
 
        if operacao == "+":
            resultado = somar(num1, num2)
        elif operacao == "-":
            resultado = subtrair(num1, num2)
        elif operacao == "*":
            resultado = multiplicar(num1, num2)
        elif operacao == "/":
            resultado = dividir(num1, num2)
        else:
            print("Operação inválida!")
            return
 
        print(f"Resultado: {resultado}")
 
    except ValueError:
        print("Erro: Entrada inválida. Digite apenas números.")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
 
calculadora()