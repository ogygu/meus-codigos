import random

tentativas_feitas = []
matriz = [["x " for _ in range(10)] for _ in range(10)]

def grade(matriz):
    print("   A ", "B ", "C ", "D ", "E ", "F ", "G ", "H ", "I ", "J")
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if (j, i) in tentativas_feitas:
                if (j, i) in posBomba:
                    matriz[i][j] = "B "
                else:
                    matriz[i][j] = f"{contar_bombas_ao_redor((j, i), posBomba)} "
    for linha in range(len(matriz)):
        print(linha, end="  ")
        for elemento in matriz[linha]:
            print(elemento, end=' ')
        print()

def bomba(colunas, linhas):
    return [(random.randint(0, colunas - 1), random.randint(0, linhas - 1)) for _ in range(10)]

def eBomba(colunas, linhas, matriz):
    global posBomba
    posBomba = bomba(colunas, linhas)
    
    print("Posição da bomba (debug): ", posBomba)
    
    while True:
        escolhaLetra = input("Escolha uma coluna pela Letra correspondente: ").upper()
        escolhaNumero = int(input("Escolha uma linha pelo Número correspondente: "))

        # Converte a letra em um índice de coluna
        escolhaColuna = ord(escolhaLetra) - ord('A')
        
        tentativa = escolhaColuna, escolhaNumero
        tentativas_feitas.append(tentativa)
        print(tentativas_feitas, tentativa)
        
        if tentativa in posBomba:
            print("Você perdeu!")
            grade(matriz)
            break
                
        else:
            grade(matriz)
            print("Continue!")

        marcador = int(input("Você quer marcar(1) ou jogar(0): "))
        if marcador == 1:
            escolhaLetra = input("Escolha uma coluna pela Letra correspondente: ").upper()
            escolhaNumero = int(input("Escolha uma linha pelo Número correspondente: "))

            escolhaColuna = ord(escolhaLetra) - ord('A')

            grade(marcar(escolhaColuna, escolhaNumero, matriz))

def contar_bombas_ao_redor(jogada, coordenadas_bombas):
    linhas = colunas = 10
    x, y = jogada
    bombas_ao_redor = 0

    for i in range(max(0, x-1), min(linhas, x+2)):
        for j in range(max(0, y-1), min(colunas, y+2)):
            if (i, j) in coordenadas_bombas and (i, j) != jogada:
                bombas_ao_redor += 1

    return bombas_ao_redor

def marcar(coluna, linha, matriz):
    matriz[linha][coluna] = "M "
    return matriz

colunas = 10
linhas = 10
grade(matriz)
eBomba(colunas, linhas, matriz)