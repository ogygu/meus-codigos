produtos = [
    {
        "nome": "Smartphone",
        "comentarios": [
            { "usuario" : "Joao", "comentario" : "Muito bom", "nota" : 9.5},
            { "usuario" : "Luigi", "comentario" : "Exelente", "nota" : 9}

        ],
        "estoque": 30,
        "preço": 1500.00
    },
    {
        "nome": "Fone de ouvido bluetooth",
        "comentarios": [
            { "usuario" : "Emanuelly", "comentario" : "otimo som", "nota" : 8},
            { "usuario" : "Catharine", "comentario" : "ainda não testei", "nota" : 5}

        ],
        "estoque": 100,
        "preço": 15.00

    },
    {
        "nome": "Tablet",
        "comentarios": [
            { "usuario" : "Arthu Benfica", "comentario" : "Muito fragil", "nota" : 4.3},
            { "usuario" : "Arthu Barcelos", "comentario" : "Exelente", "nota" : 10}

        ],
        "estoque": 35,
        "preço": 500.00
    },
    {
        "nome": "Smartwatch",
        "comentarios": [
            { "usuario" : "Maria Clara", "comentario" : "Perfeitoo", "nota" : 10},
            { "usuario" : "Vitória", "comentario" : "Me serviu muito bem", "nota" : 7}

        ],
        "estoque": 15,
        "preço": 450.00
    }
]

def numeroProdutos(produtos):
    return len(produtos)

def informaçãoProduto(produtos):
    informações = []
    for i in produtos:
        nome = i["nome"]
        NumComentarios = len(i["comentarios"])
        notaMedia = sum(comentario["nota"] for comentario in i["comentarios"])/NumComentarios
        informações.append({"nome": nome, "numero de comentarios" : NumComentarios, "nota media": notaMedia})
    return informações

def ultimoComentario(produtos):
    ultimoComentario = []
    for i in produtos:
        comentario = i["comentarios"][-1]["comentario"]
        ultimoComentario.append({"nome": i["nome"], "ultimo comentario": comentario })
    return ultimoComentario

def terceiroProduto(produtos):
    terceiro = produtos[2]
    return {"nome": terceiro["nome"],"estoque" : terceiro["estoque"]}

def produtosAcimaDaMedia(produtos):
    notas = [comentario["nota"] for i in produtos for comentario in i["comentarios"]]
    media = sum(notas)/len(notas)
    acimaMedia = [i["nome"] for i in produtos if sum(comentario["nota"] for comentario in i["comentarios"] )/ len(i["comentarios"]) > media]
    return acimaMedia

 
def reduzirPrecos(produtos):
    for i in produtos:
        i["preço"] = i["preço"]*0.9
    return produtos

def venderQuartoProduto(produtos):
    produtos[3]["estoque"] = produtos[3]["estoque"] - 1
    return produtos


print(f"Numero de produtos:{numeroProdutos(produtos)}")

print("\nInformações dos produtos:")
for info in informaçãoProduto(produtos):
    print(info)

print("\nUltimos comentarios:")
for comentario in ultimoComentario(produtos):
    print(comentario)

print(f"\n3º Produto:{terceiroProduto(produtos)}")

print(f"\nProdutos com nota acima da média:{produtosAcimaDaMedia(produtos)}")

print("\nLista de produtos com preços reduzidos em 10%")
for produto in reduzirPrecos(produtos):
    print(produto)

print("\nLista de produtos após a venda do 4º item:")
for produto in venderQuartoProduto(produtos):
    print(produto)
