#Ana precisa de um programa simples para gerenciar suas tarefas diárias. Ela quer poder adicionar, visualizar e remover tarefas de uma lista.
#
#Crie um programa com um menu interativo que permita ao usuário adicionar, visualizar e remover tarefas. Use uma lista para armazenar as tarefas.
#
#Exemplo de entrada:
#
#1. Adicionar tarefa 
#2. Visualizar tarefas 
#3. Remover tarefa 
#4. Sair
#Escolha uma opção: 1
#
#Saída esperada:
#
#Digite a tarefa: Estudar Python
#Tarefa adicionada!
#
#Caso selecione a opção 2 ao adicionar uma tarefa:
#
#Tarefas:
#1. Estudar Python
#
#Caso selecione a opção 3 com uma tarefa adicionada:
#
#Digite o número da tarefa a ser removida: 1
#Tarefa 'Estudar Python' removida!
#
#Caso selecione a opção 3 sem uma tarefa adicionada:
#
#Digite o número da tarefa a ser removida: Estudar Python
#Erro: Nenhuma tarefa para remover.
#
#Caso selecione a opção 3 com uma opção inválida:
#
#Escolha uma opção: 3
#Digite o número da tarefa a ser removida: ABC
#Erro: Entrada inválida! Digite um número.
#
#Caso selecione nenhuma das opções listadas:
#
#Escolha uma opção: 5
#Erro: Opção inválida! Escolha uma opção entre 1 e 4.
#
#Caso selecione a opção 4:
#
#Escolha uma opção: 4 
#Saindo do gerenciador de tarefas. Até mais!

def gerenciador_tarefas():
    tarefas = []
 
    while True:
        print("\n1. Adicionar tarefa")
        print("2. Visualizar tarefas")
        print("3. Remover tarefa")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
 
        if opcao == "1":
            tarefa = input("Digite a tarefa: ").strip()
            if tarefa:  # Verifica se a string não está vazia
                tarefas.append(tarefa)
                print("Tarefa adicionada!")
            else:
                print("Erro: A tarefa não pode estar vazia.")
 
        elif opcao == "2":
            if tarefas:
                print("\nTarefas:")
                for i, tarefa in enumerate(tarefas, 1):
                    print(f"{i}. {tarefa}")
            else:
                print("Nenhuma tarefa cadastrada.")
 
        elif opcao == "3":
            if not tarefas:
                print("Erro: Nenhuma tarefa para remover.")
                continue
 
            try:
                indice = int(input("Digite o número da tarefa a ser removida: ")) - 1
                if 0 <= indice < len(tarefas):
                    removida = tarefas.pop(indice)
                    print(f"Tarefa '{removida}' removida!")
                else:
                    print("Erro: Índice inválido! Digite um número válido.")
            except ValueError:
                print("Erro: Entrada inválida! Digite um número.")
 
        elif opcao == "4":
            print("Saindo do gerenciador de tarefas. Até mais!")
            break
 
        else:
            print("Erro: Opção inválida! Escolha uma opção entre 1 e 4.")
 
gerenciador_tarefas()