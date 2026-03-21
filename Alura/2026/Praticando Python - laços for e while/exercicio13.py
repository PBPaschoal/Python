#João está desenvolvendo um sistema de cadastro para um site de leitura. 
#Ele precisa garantir que os usuários insiram um nome de usuário e uma senha válidos. As regras são as seguintes:
#O nome de usuário deve ter pelo menos 5 caracteres.
#A senha deve ter pelo menos 8 caracteres.
#João quer que o sistema continue solicitando as informações até que ambas as condições sejam atendidas. 
#Quando o usuário insere dados válidos, o programa deve exibir a mensagem: "Cadastro realizado com sucesso!".
#Crie um programa que implemente essa lógica usando um laço while.
#Saída esperada:
#Digite seu nome de usuário: user
#Digite sua senha: 123
#O nome de usuário deve ter pelo menos 5 caracteres.
#Digite seu nome de usuário: user22
#Digite sua senha: 12345
#A senha deve ter pelo menos 8 caracteres.
#Digite seu nome de usuário: user22
#Digite sua senha: 123456789
#Cadastro realizado com sucesso!

while True:
    nome_usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    if len(nome_usuario) < 5:
        print("O nome de usuário deve ter pelo menos 5 caracteres.")
        continue

    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
        continue

    print("Cadastro realizado com sucesso!")
    break