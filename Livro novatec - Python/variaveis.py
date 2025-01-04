a = 3 * 0.1
b = 1.95
c = 9 / 4
d = 0b10 #Base 2 - binário
e = 0x10 #Base 16 - hexadecimal
f = 0o10 #Base 8 - octal
print("----------------")
print(f"a = {a}")
print(f"a + b = {b + c}")
print(f"d = {d}, e = {e}, f = {f}")

#Variáveisa do tipo Lógico
#Operadores relacionais
g = 1
h = 5
i = 2
j = 1
print("----------------")
print("Operadores relacionais")
print(f"g = {g}, h = {h}, i = {i}, j = {j}")
print("g é igual a h?")
if (g == b):
    print(True)
else:
    print(False)

print("h é maior que g?")
if(h > g):
    print(True)
else:
    print(False)

print("g é menor que h?")
if(g < h):
    print(True)
else:
    print(False)

print("g é igual a j?")
if(g == j):
    print(True)
else:
    print(False)

print("h é maior ou igual a g?")
if(h >= g):
    print(True)
else:
    print(False)

print("i é menor ou igual a h?")
if(i <= h):
    print(True)
else:
    print(False)

print("j é diferente de g?")
if(j != g):
    print(True)
else:
    print(False)

print("j é diferente de h?")
if(j != h):
    print(True)
else:
    print(False)

nota = 8
media = 7
aprovado = nota > media
print("----------------")
print(f"Nota = {nota}; Média = {media}: O aluno está aprovado? {aprovado}")

aA = 4
bB = 10
cC = 5.0
dD = 1
fF = 5
print("----------------")
print(f"{aA} == {cC}? {aA == cC}")
print(f"{aA} < {bB}? {aA < bB}")
print(f"{dD} > {bB}? {dD > bB}")
print(f"{cC} != {fF}? {cC != fF}")
print(f"{aA} == {bB}? {aA == bB}")
print(f"{cC} < {dD}? {cC < dD}")
print(f"{bB} > {aA}? {bB > aA}")
print(f"{cC} >= {fF}? {cC >= fF}")
print(f"{fF} >= {cC}? {fF >= cC}")
print(f"{cC} <= {cC}? {cC <= cC}")
print(f"{cC} <= {fF}? {cC >= fF}")

#Operadores Lógicos
vA = True
vB = False
vC = True
print("----------------")
print("Operadores Lógicos")
print(f"{vA} and {vA}? {vA and vA}")
print(f"{vB} and {vB}? {vB and vB}")
print(f"not {vC}? {not vC}")
print(f"not {vB}? {not vB}")
print(f"not {vA}? {not vA}")
print(f"{vA} and {vB}? {vA and vB}")
print(f"{vB} and {vC}? {vB and vC}")
print(f"{vA} or {vC}? {vA or vC}")
print(f"{vB} or {vC}? {vB or vC}")
print(f"{vC} or {vA}? {vC or vA}")
print(f"{vC} or {vB}? {vC or vB}")
print(f"{vC} or {vC}? {vC or vC}")
print(f"{vB} or {vB}? {vB or vB}")