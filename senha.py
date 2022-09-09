while True:
    senha = str(input('Insira a senha: '))
    senha_correta= 'Senha123@'
# Se a senha estiver correta ira imprimir "Voce esta Logado" e se estiver errada irá imprimir "INCORRETA"
    if senha == senha_correta:
        print('Você está logado')    
        break 

    else:
        print('Senha errada, tente mais uma vez')      
    

       

