#1 - Crie uma lista para cada informação a seguir:
#Lista de números de 1 a 10;
#Lista com quatro nomes;
#Lista com o ano que você nasceu e o ano atual.


lista_nome = ['Ana', 'Jho', 'Helga', 'Fabi']
lista_numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_ano = [2003, 2026]


#2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
print('-------------------------')
for numero in lista_numero:
    print(f'\n- {numero}\n')

print('-------------------------')
for nome in lista_nome:
    print(f'\n- {nome}\n')
  
  
#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.  
print('-------------------------')
soma_impares = 0 

for i in range (1, 11, 2):
    soma_impares += i
    print(f'\n- {soma_impares}\n')
    
#4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.    
print('-------------------------')    
for i in range(10, 0, -1):
    print(f'\n- {i}\n')
    
      
#6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.    
lista_numeros = [10, 5, 8, 3, 7]
soma = 0

print('-------------------------')

try:
    for numero in lista_numeros:
        soma += numero
    print(f'\nSoma dos elementos: {soma}\n')
except Exception as e:
    print(f'\nOcorreu um erro: {e}\n')
    
    
#7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.    
print('-------------------------')    
lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f'\nMédia dos valores: {media}\n')
except ZeroDivisionError:
    print('\nA lista está vazia, não é possível calcular a média.\n')
except Exception as e:
    print(f'\nOcorreu um erro: {e}\n')
    