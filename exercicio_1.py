"""
algoritimo que recebe uma lista de valores
e retorna a soma e a media
Autor: Marcos Alexandre Alves Araujo
data: 02/09/2022 10:13
"""
#definição de função
def soma(numeros):
    soma = sum(numeros)
    print(f'A soma e {soma}')



#função da média
def media(valores):
        avg = sum(valores)/ len(valores)
        print(f'\nA media é {avg}')



#criação da lsita

lista = []

for a in range(5):
    lista.append(int(input('insira um valor: ')))
soma(lista)
media(lista)
