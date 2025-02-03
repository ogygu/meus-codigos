personagens = {
    "zangief": {
        "forca": 100,
        "vida": 150,
        "velocidade": 0,
        "magia": 0,
    },
    "ken": {
        "forca": 50,
        "vida": 100,
        "velocidade": 50,
        "magia": 50
    },
    "ryu": {
        "forca": 75,
        "vida": 100,
        "velocidade": 50,
        "magia": 25
    },
    "chun-li": {
        "forca": 25,
        "vida": 75,
        "velocidade": 125,
        "magia": 50
    }
}

lutas = [
    {"p1": "ryu", "p2": "ryu", "venceu": "p1"},
    {"p1": "ken", "p2": "zangief", "venceu": "p2"},
    {"p1": "ken", "p2": "chun-li", "venceu": "p1"},
    {"p1": "ken", "p2": "ken", "venceu": "p2"},
    {"p1": "zangief", "p2": "zangief", "venceu": "p2"},
    {"p1": "ryu", "p2": "chun-li", "venceu": "p2"},
    {"p1": "chun-li", "p2": "chun-li", "venceu": "p1"},
]

# a. Para cada personagem, mostre na tela a soma das estatísticas do personagem
def soma_estatisticas(personagens):
    estatisticas = {}
    for nome, stats in personagens.items():
        total = sum(stats.values())
        estatisticas[nome] = total
    return sorted(estatisticas.items(), key=lambda x: x[1])

# b. Mostre na tela os valores médios das estatísticas de todos os personagens
def media_estatisticas(personagens):
    total_stats = {"forca": 0, "vida": 0, "velocidade": 0, "magia": 0}
    num_personagens = len(personagens)
    
    for stats in personagens.values():
        for key in total_stats:
            total_stats[key] += stats[key]
    
    media_stats = {key: total / num_personagens for key, total in total_stats.items()}
    return media_stats

# c. O nome e os dados do personagem escolhido com mais frequência
def personagem_mais_escolhido(lutas):
    escolhas = {}
    for luta in lutas:
        for p in ["p1", "p2"]:
            personagem = luta[p]
            if personagem in escolhas:
                escolhas[personagem] += 1
            else:
                escolhas[personagem] = 1
    
    mais_escolhido = sorted(escolhas.items(), key=lambda x: (-x[1], x[0]))[0][0]
    return mais_escolhido, personagens[mais_escolhido]

# d. O nome e os dados do personagem que levou a um maior número de vitórias
def personagem_mais_vitorioso(lutas):
    vitorias = {}
    for luta in lutas:
        vencedor = luta["venceu"]
        personagem = luta[vencedor]
        if personagem in vitorias:
            vitorias[personagem] += 1
        else:
            vitorias[personagem] = 1
    
    mais_vitorioso = sorted(vitorias.items(), key=lambda x: (-x[1], x[0]))[0][0]
    return mais_vitorioso, personagens[mais_vitorioso]

# Exibindo as informações
print("Soma das estatísticas dos personagens (em ordem ascendente):")
for nome, total in soma_estatisticas(personagens):
    print(f"{nome}: {total}")

print("\nValores médios das estatísticas de todos os personagens:")
for stat, media in media_estatisticas(personagens).items():
    print(f"{stat}: {media:.2f}")

mais_escolhido, dados_mais_escolhido = personagem_mais_escolhido(lutas)
print(f"\nPersonagem mais escolhido: {mais_escolhido}")
print(dados_mais_escolhido)

mais_vitorioso, dados_mais_vitorioso = personagem_mais_vitorioso(lutas)
print(f"\nPersonagem mais vitorioso: {mais_vitorioso}")
print(dados_mais_vitorioso)