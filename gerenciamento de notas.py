def informaçãoTurma():
    with open("informaçãoTurma.txt","w") as arq:
        conteudo = input("digite as informacoes da turma :")
        arq.write(conteudo + "\n")

    with open("informaçãoTurma.txt", "r") as arq :
        conteudoLido = arq.read()

    return f"informações salvas com sucesso"

def aluno_nota():
    aprovados = []
    reprovados = []
    with open("aluno_nota.txt", "w") as arq :
        quantidade = int(input("digite a quantidade de alunos: "))
        for i in range(quantidade):
            aluno =str(input(f"digite o nome do {i+1}º aluno: "))
            nota = float(input(f"digite a nota do {i+1}º aluno: "))
            if nota >= 60 :
                print(f"{aluno} aprovado") 
                aprovados.append(aluno)     
            else : 
                print(f"{aluno} reprovado ")
                reprovados.append(aluno)

            arq.write(f"{aluno} : {nota}\n")
            print("----------------------------------------------")
    
    with open("aluno_nota.txt","r")  as arq :
        conteudoLido = arq.read()
        
    return f"informações salvas com sucesso"  

def aprovados():
    aprovados = []  
    with open("aluno_nota.txt","r") as arq :
        for linha in arq :
            aluno, nota = linha.split(" : ")
            if float(nota) >= 60 : 
                aprovados.append(aluno)     
    return f"Alunos aprovados : {', '.join(aprovados)}"

def reprovados():
    reprovados = []

    with open("aluno_nota.txt","r") as arq :
        for linha in arq:
            aluno, nota = linha.split(" : ")
            if float(nota)< 60 :
                reprovados.append(aluno)
    
    return f"Alunos reprovados : {', '.join(reprovados)}"

def calcularMedia():
    totalNotas = 0
    quantidadeAlunos = 0

    with open("aluno_nota.txt","r") as arq :
        for linha in arq :
            aluno,nota = linha.split(" : ")
            totalNotas += float(nota)
            quantidadeAlunos += 1 
    if quantidadeAlunos == 0 :
        return "Nenhum aluno encontrado para calcular a média "
    media = totalNotas/quantidadeAlunos
    return f"Média de todos os alunos : {media :.2f}"

def salvarDados():
    with open("backup.txt","w") as backup :
        with open("informaçãoTurma.txt", "r") as turma :
            backup.write("Informações da Turma: \n")
            backup.write(turma.read() + "\n")
        
        with open("aluno_nota.txt","r") as notas :
            backup.write("Notas dos Alunos: \n")
            backup.write(notas.read() + "\n")
    
    return "Dados salvos com sucesso no arquivo backup.txt"

while True :
    pergunta = str(input("digite:\n(A) -> para definir informações da turma\n(B)-> inserir aluno e nota\n(C)-> exibir alunos aprovados\n(D)->exibir alunos reprovados \n(E)-> exibir  média \n(F)-> salvar dados em disco\n(G)->sair do programa\n:")).lower()
    if pergunta == "A".lower():
        print(informaçãoTurma())

    elif pergunta ==  "B".lower():
        print(aluno_nota())

    elif pergunta == "C".lower():
        print(aprovados())

    elif pergunta == "D".lower():
        print(reprovados())

    elif pergunta == "E".lower():
        print(calcularMedia())

    elif pergunta == "F".lower():
        print(salvarDados())

    elif pergunta == "G".lower():
        print("Saindo do programa...")
        break

    else : 
        print("Opção inválida. Tente novamente")
        





    

