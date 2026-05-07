#1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
while True:
    num1 = input('\nDigite um número: ')

    if num1.isdigit():
        num_final = int(num1)
        
        if num_final % 2 == 0:
            print('\nNúmero par!')
        
        else:
            print('\nNúmero ímpar')
            
        break
    
    else:
        print('\nDigite um número válido!')
 