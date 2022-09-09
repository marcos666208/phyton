# Menssagem que pergunta o tamanho dos lados
l1  =  float(input('qual o tamanho do primeiro lado: '))
l2  =  float(input('qual o tamanho do segundo lado: '))
l3  =  float(input('qual o tamanho do terceiro: '))
# Operação para saber se é possivel ou não construir um triângulo
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmento PODEM FORMAR um triângulo : ', end='')
# Operação Para Saber se e Possivel Fazer Um Triângulo EQUILÁTERO
    if l1 == l2 == l3:
        print('EQUILÁTERO .')
# Operação Para Saber se e Possivel Fazer Um Triângulo ESCALENO
    elif l1 != l2 != l3 != l1:
        print('ESCALENO .')
# Operação Para Saber se e Possivel Fazer Um Triângulo ISÓCELES
    else:
        print('ISÓCELES .')
else:
    print('Os segmento acima NÃO PODEM formar um triangulo')
    # Pedindo para o usuário inserir uma senha

   