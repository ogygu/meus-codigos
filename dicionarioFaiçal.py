#1
"""estado = dict()
brasil = list()

for i in range(0,3):
    estado['UF'] = str(input(f'{i + 1}º Unidade Federativa :'))
    estado['Sigla'] = str(input(f'{i + 1}º Sigla do Estado:'))
    print("--------------------------------------------------")
    brasil.append(estado.copy())
print(brasil)
print("--------------------")
for e in brasil:
    for v in e.values():
        print(f"os valores são: {v}\n")
        print("-----------------------")
    for k in e.keys():
        print(f'as chaves são: {k}\n')
        print("----------------------")
    for k , v in e.items():
        print(f'{k} = {v}\n')"""


#2
"""estoque = {
    "banana": 1000,
    "alface": 500,
    "batata": 2000,}

def atualizar_estoque(produto, quantidade_vendida):
    if produto in estoque:
        if estoque[produto] >= quantidade_vendida:
            estoque[produto] -= quantidade_vendida
            print(f"Venda realizada! Novo estoque de {produto}: {estoque[produto]}")
        else:
            print(f"Estoque insuficiente! Estoque atual de {produto}: {estoque[produto]}")
    else:
        print(f"Erro: O produto '{produto}' não existe no estoque.")

# Loop para solicitar entrada do usuário até que ele decida sair
while True:
    print("\nProdutos disponíveis e seus estoques:")
    for item, quantidade in estoque.items():
        print(f"- {item}: {quantidade} unidades")

    produto = input("\nDigite o nome do produto (ou 'sair' para encerrar): ").lower()
    if produto == 'sair':
        print("Encerrando o programa.")
        break

    quantidade_vendida = int(input("Digite a quantidade vendida: "))
    if quantidade_vendida < 0:
        print("Erro: A quantidade vendida não pode ser negativa.")
    else:
        atualizar_estoque(produto, quantidade_vendida)"""  
      






