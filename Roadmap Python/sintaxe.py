# Sintaxe Básica do Python
print("Hello, Python!")

if True:
    print("Praticando!")

# Variáveis e Tipos de Dados
idade = 32
altura = 1.74
nome = "Bruno"
esta_certo = True

print(f"Sua idade é {idade}")
print(f"E a sua altura é {altura}")
print(f"Você se chama {nome}")
print(f"Você é um estudante de programação? {esta_certo}")

# Estruturas Condicionais
print (f"{nome},", end=" ")
if idade >= 18:
    print("você é maior de idade.")
else:
    print("você é menor de idade.")