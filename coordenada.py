#4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

#Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
#Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
#Terceiro Quadrante: os valores de x e y devem ser menores que zero;
#Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
#Caso contrário: o ponto está localizado no eixo ou origem.

def quadr():
    if coord_x > 0 and coord_y > 0:
        print('\nVocê está no primeiro quadrante\n')
    elif coord_x < 0 and coord_y > 0:
        print('\nVocê está no segundo quadrante\n')
    elif coord_x < 0 and coord_y < 0:
        print('\nVocê está no terceiro quadrante\n')
    elif coord_x > 0 and coord_y < 0:
        print('\nVocê está no quarto quadrante\n')
    else:
        print('\nVocê está no eixo de origem\n')
        
coord_x = int(input('\nDigite a primeira coordenada: '))
coord_y = int(input('\nDigite a segunda coordenada: '))

quadr()