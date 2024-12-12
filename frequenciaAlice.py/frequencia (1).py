import time

def removerSimbolos(texto):
    
    espaço = ' '
    for i in texto:
        if i.isalpha():
            espaço += i
        else:
            espaço += ' '
    return espaço  

def selecionarPalavras(texto):
    resultado_semSimbolo = removerSimbolos(texto)
    minusculo = resultado_semSimbolo.lower()
    palavras = minusculo.split()
    return palavras

    
def carregarPalavrasArquivo(texto):
    with open(texto,'r') as arq :
        conteudo = arq.read()
    return selecionarPalavras(conteudo)

def frequenciaPalavrasDicionario(palavrasListadas):
    dicionarioAlice = {}
    for i in palavrasListadas :
        if i in dicionarioAlice:
            dicionarioAlice[i] += 1
             
        else :
            dicionarioAlice[i] = 1
    return dicionarioAlice 



def verificrFrquencia(escolherPalavras, dicionarioAlice):
    if escolherPalavras in dicionarioAlice :
        return dicionarioAlice[escolherPalavras]
    else :
        print("essa palavra nao existe no dicionario")
        return 0




arquivo = 'alice.txt'


#escolherP = str(input("Digite a palavra em ingles a ser encontrada no arquivo:")).lower()"""  
resultado = carregarPalavrasArquivo(arquivo)
frequencia = frequenciaPalavrasDicionario(resultado)
print(frequencia)
#frequencia2 = verificrFrquencia(escolherP,frequencia)"""

#print(f" {escolherP}:{frequencia2}  " ) 