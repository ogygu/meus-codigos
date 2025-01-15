import os

def dadosProduto():
    with open("dadosProduto.txt","w") as arq:
        while True:
            nome = str(input("Digite o nome do produto:"))
            codigo = int(input("Digite o código do produto:"))
            preço =float(input("Digite o preço do produto:"))
            quantidade = int(input("Digite a quantidade do produto:"))
            arq.write(f"{nome} : {codigo} : {preço} : {quantidade}\n")
            print("-------------------------------------------------")
            ask = str(input("deseja adicionar mais produtos?(S/N)")).lower()
            if ask in "n":
                break
    return f"Informações salvas com sucesso"

def retirarProduto():
    produtos = []
    if os.path.exists("dadosProduto.txt"):
        with open("dadosProduto.txt", "r") as arq:
            produtos = [linha.strip().split(":") for linha in arq.readlines()]
    
    codigo = int(input("Digite o código do produto a ser retirado: "))
    quantidade_retirada = int(input("Digite a quantidade a ser retirada: "))
    
    for produto in produtos:
        if int(produto[1]) == codigo:
            produto[3] = str(int(produto[3]) - quantidade_retirada)
            break
    
    with open("dadosProduto.txt", "w") as arq:
        for produto in produtos:
            arq.write(":".join(produto) + "\n")
    
    return "Produto retirado com sucesso"

def relatorioGeral():
    if os.path.exists("dadosProduto.txt"):
        with open("dadosProduto.txt","r") as arq:
            produtos = arq.readlines()
        return "Relatório Geral\n" + "".join(produtos)
    else :
        return "Nenhum produto encontrado"
            
def produtosNaoDisponiveis():
    if os.path.exists("dadosProduto.txt"):
        with open("dadosProduto.txt", "r") as arq:
            produtos = [linha.strip().split(":") for linha in arq.readlines()]
            naoDisponiveis = [produto for produto in produtos if int(produto[3]) <= 0]
            return "Produtos não disponíveis:\n" + "\n".join([":".join(produto) for produto in naoDisponiveis])
    else:
        return "Nenhum produto encontrado"



while True:
    pergunta = str(input("Digite:\n(A)-> Adicionar dados do produto\n(B)-> Retirar produtos\n(C)-> Relatório Geral\n(D)-> Produtos não disponíveis\n(E)-> Sair do programa\n:")).lower()
    if pergunta == "a":
        print(dadosProduto())
    elif pergunta == "b":
        print(retirarProduto())
    elif pergunta == "c":
        print(relatorioGeral())
    elif pergunta == "d":
        print(produtosNaoDisponiveis())
    elif pergunta == "e":
        print("Programa encerrado")
        break
    else :
        ("Opções indisponiveis")
    
    

