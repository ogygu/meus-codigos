# coding: utf - 8

from collections import deque

def adicionarPaciente(fila):
    nome = str(input("Digite o nome do paciente"))
    if len(fila) == 0:
        senha = 1
    else :
        senha = fila[-1]["senha"] + 1
    fila.append({"nome": nome, "senha": senha})
    return f"O paciene {nome} foi adicionado com sucesso"


def menu():
    fila = deque()
    while True:
        print("---AGENDAMENTO MÉDICO---")
        print("1 -> Adicionar paciente\n2 -> Chmamar Próximo Paciente\n3 -> Exibir fila de pacientes\n4 -> Sair")
        selecionar = str(input("Digite a opção que se deseja:"))
        if selecionar == "1":
            adicionarPaciente()
