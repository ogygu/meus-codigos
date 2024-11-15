"""
#1
def verificação():
    x = int(input('digite um numero :')) 
    if x % 2 == 0 :
        print(f"{x} é um numero par ")
        return True
    else :
        print(f"{x} é impar")
        return False
verificação()"""
"""
#2
def tamanho(x,y):
    if x > y :
        print(f"{x} é maior que {y}")
    elif x == y :
        print(f"{x} e {y} são iguais ")
    else:
        print(f"{y} é maior que {x}")

num1 = int(input("digite um numero :"))
num2 = int(input("digite um numero :"))

tamanho(num1,num2)"""

"""
#3
def soma(a , b):

    soma1 = sum(range(a+1, b))
    return soma1
      
       

num1 = int(input("digite um numero :"))
num2 = int(input("digite um numero :"))   

resultado = soma(num1,num2)
print(resultado)"""

"""
#4
def multiplicação(x,y):
    mult = x * y
    return mult
   
   

num1 = int(input("digite um numero :"))
num2 = int(input("digite um numero :"))  

resultado = multiplicação(num1,num2)
print(resultado)"""
"""


#5
def multiplicação_manual():
    num= int(input('digite um numero:'))
    multiplicação = int(input(f'vai ser {num} X ? :'))
    cont = 0
    for i in range(1,multiplicação + 1):
        cont += num
    print(f"{num}X{multiplicação} = {cont}") 
multiplicação_manual() """      

"""
#6
def potencia(x,y):
    Potencia = x**y
    return Potencia

num1 = int(input("digite um numero :"))
num2 = int(input("digite um numero :"))  

resultado = potencia(num1,num2)
print(resultado)"""
"""
#7
def potencia_manual():
    num = int(input('digite um numero inteiro :'))
    potencia = int(input(f'{num}**?:'))
    cont = 1
  
    for i in range(potencia):
        cont*= num
            
    print(f'{num}**{potencia} = {cont}')
potencia_manual()"""   

"""
#8
def vweificar_numero_primo(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            print("não é  primo")
            return False
    print(" é primo ")    
    return True

num = int((input('digite um numero para ver se é primo:')))
resultado = vweificar_numero_primo(num)"""



"""
#9
def fat(x):
    if x <= 1:
        print("digite numero maiores que 1")
    contador = 1
    for i in range(1,x + 1):
        contador*= i
    return contador

num = int(input('digite um numero:'))
resultado = fat(num)
print(resultado)"""    

"""
#10
def arranjo():

    def fatorial_x(x):
        if x <= 1 :
            print('digite numeros maiores que 1')
        contador = 1    
        for i in range(1, x + 1):
            contador*= i
        return contador
    numN = int(input('digite um numero inteiro:'))
    resultadoN = fatorial_x(numN)
    print("---------------------------------------------------------------")
    numP = int(input('digite um numero inteiro P para calcular o arranjo :'))
    subtração = numN - numP
    def fatorial_Subtração(s):
        if s <= 1 :
            print('digite numeros maiores que 1')
        contador = 1    
        for i in range(1, s + 1):
            contador*= i
        return contador
    resultadoSub = fatorial_Subtração(subtração)

    Arranjo = resultadoN/resultadoSub
    print(Arranjo)

arranjo()"""


"""
#11
def combinação():
    def fatorial_x(x):
        if x <= 1 :
            print('digite numeros maiores que 1')
        contador = 1    
        for i in range(1, x + 1):
            contador*= i
        return contador
    numN = int(input('digite um numero inteiro:'))
    resultadoN = fatorial_x(numN)
    print("---------------------------------------------------------------")
    numP = int(input('digite um numero inteiro P para calcular o arranjo :'))
    subtração = numN - numP
    def fatorial_Subtração(s):
        if s <= 1 :
            print('digite numeros maiores que 1')
        contador = 1    
        for i in range(1, s + 1):
            contador*= i
        return contador
    resultadoSub = fatorial_Subtração(subtração)
    resultadoP = fatorial_x(numP)

    Combinação = resultadoN/(resultadoP *resultadoSub)
    print(Combinação)
combinação() """



