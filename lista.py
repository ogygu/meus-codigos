"""
#1
lista = []
for i in range(100):
    if i % 2 == 0:
        lista.append(0)
    else:
        lista.append(1)
print(lista)"""

"""
#2
lista1 = []
lista2 = []
for i in range(5):
    num = int(input("Insira um número para a lista 1:"))
    lista1.append(num)
print("--------------------------------------")
for j in range(10):
    num = int(input("Insira um número para a lista 2:"))
    lista2.append(num)
    lista3 = lista1 + lista2
    print("--------------------------------------")
    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")
    print(f"Lista 3: {lista3}")"""

"""
#3
notas = []
matricula = []

for i in range(50):
    notas.append(float(input(f"informe a {i+1}° nota :")))
    matricula.append(int(input(f"informe o {i + 1}° nuemro da matricula")))
    print("--------------------------------------------------------------")

print(f"Aqui estão as notas : {notas}")
media = sum(notas)/50
print(f"A média é : {media}")

notas_abaixo = 0
notas_acima = 0 

for notas in notas :
    if notas > media:
        notas_acima = notas_acima + 1
       
    if notas < media :
        notas_abaixo = notas_abaixo + 1
        

print(f"foram acima da media : {notas_acima}")
print(f"as notas abaixo foram : {notas_abaixo}") """
"""
#4
lista = []
for i in range(10):
    num = int(input("Insira um número inteiro:"))
    lista.append(num)
    valorM = int(input("Insira o valor que você quer achar na sua lista:"))
    position = 0
    if valorM in lista:
        position = lista.index(valorM)
        print(f"A posição do valor que você pediu é: {position}")
    else:
        print("O valor, m, não se encontra na lista")

#5
elementos = []

for i in range(12): 
    elementos.append(int(input(f"digite o {i+1}º elemento inteiro")))
    print("--------------------------------------------------------")

print(f"os 12 elementos são :{elementos}")  
elementos.sort(reverse=True)
print(f"os elementos invertidos : {elementos}") """

"""
#6
lista = []
for i in range(12):
    lista.append(int(input(f"digite o {i + 1}º numero :")))

x = int((input("digite a posição   de X :")))
y = int(input("digite a posição de Y :"))
posição1 = lista.index(x)
posição2 = lista.index(y)
soma = posição1 + posição2
print(soma)"""

"""
#7
lista=[]
for i in range(4):
    lista.append(int(input(f"digite o {i + 1}º numero inteiro ")))

print(lista)  
maior_elemento = lista[0]
indice_maior = 0

for i in range(1,len(lista)):
    if lista[i] > maior_elemento :
        indice_maior = i
"""


"""
#8
idade=[]
for i in range(4):
    idade.append(f"qual a idade do { i + 1}º aluno:")

print(idade)

maior_que_13 = 0
menor_que_13 = 0

for idade in idade :
    if idade > 13 :
        maior_que_13 = maior_que_13 + 1
    if idade < 13 :
        menor_que_13 = menor_que_13 + 1

print(maior_que_13)
print(menor_que_13) """           
