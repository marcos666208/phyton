#Criação do menu
while True:
    print("""

Menu
----
1 - Adição
2 - Subtração
3 - Divisão
4 - Multiplicação
5 - Sair

""")
#Definindo as operações matematicas e imprimir a taboada
    opção = int(input("Escolha uma opção:"))
    if opção == 5:
        break
    elif opção >= 1 and opção < 5:
        n = int(input("Tabuada de:"))
        x = 1
        while x <= 10:
            #Opção para adição
            if opção == 1:
                print(f"{n} + {x} = {n + x}")
            #Operação para Subtração 
            elif opção == 2:
                print(f"{n} - {x} = {n - x}")
            #Operação para Divisão 
            elif opção == 3:
                print(f"{n} / {x} = {n / x:5.4f}")
            #Operaçao para Multiplicação 
            elif opção == 4:
                print(f"{n} x {x} = {n * x}")
            x = x + 1
    else:
        #Se nenhuma das opções listadas forem escolhidas sera imprimido "Operação inválida"
        print("Opção inválida!")