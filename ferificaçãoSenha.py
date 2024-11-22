def atualizaçãoSenha():
    senhaAntiga = []
    for i in range(5):
        digitar = int(input(f'digite o {i+1} º numero da sua antiga senha:'))
        if  digitar < 0 or digitar > 9  :
            print('Só são permitidos numeros inteiros de 0 a 9')
            print('-----------------------------------------------')
            return atualizaçãoSenha()
        senhaAntiga.append(digitar)       
    print("------------------------------------------------------------------")
    senhaNova = []
    for j in range(5): 
        atualizar= int(input(f'digite o {j+1}º numero para atualizar sunha senha:'))
        if  atualizar < 0 or atualizar > 9  :
            print('Só são permitidos numeros inteiros de 0 a 9')
            print('-----------------------------------------------')
            return atualizaçãoSenha()
        senhaNova.append(atualizar)

    if senhaAntiga != senhaNova :
        print('parabens!!!')
        print('Sua senha foi atualizada') 
    else :
        print('Não pode repetir a mesma senha')
        print('Digite novamente')
        print('-------------------------------') 
        return atualizaçãoSenha()
    print('-------------------------------------')  
    print(f'A sua senha antiga é : {senhaAntiga}\ne sua senha atualizada é : {senhaNova}')
    
atualizaçãoSenha()       
    
    
    