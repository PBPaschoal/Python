#Miguel está desenvolvendo um sistema de cupons de desconto e precisa de uma forma para aplicar diferentes taxas de desconto sobre os valores das compras.
#Diante deste problema, crie uma closure que gere uma função capaz de calcular o preço final com um desconto fixo definido pelo usuário.
#Exemplo de entrada:
#Digite a porcentagem de desconto: 10 
#Digite o valor da compra: 200
#Saída esperada:
#Preço final com desconto: 180.0

def criar_desconto(porcentagem):  

   def calcular_preco(valor):  

       return valor - (valor * (porcentagem / 100))  

   return calcular_preco 

desconto = float(input("Digite a porcentagem de desconto: "))  

calcular_preco_final = criar_desconto(desconto) 

valor = float(input("Digite o valor da compra: "))  

print(f"Preço final com desconto: {calcular_preco_final(valor)}") 