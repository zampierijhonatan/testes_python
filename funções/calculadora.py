
adicao = lambda x, y: x + y
subtracao = lambda x, y: x - y
multiplicacao = lambda x, y: x * y
divisao = lambda x, y: x / y if y != 0 else 'Erro: Divisão por 0'

        
def calc():
    while True:
        try: 
            x = float(input('Digite o primeiro número: '))
            y = float(input('\nDigite o segundo número: '))
            operacao = input('\nEscolha a operação: ( + | - | * | / ): ')

            if operacao == '+':
                print(f'\nO resultado é: {adicao(x, y)}')
                break
            elif operacao == '-':
                print(f'\nO resultado é: {subtracao(x, y)}')
                break
            elif operacao == '*':
                print(f'\nO resultado é: {multiplicacao(x, y)}')
                break
            elif operacao == '/':
                print(f'\nO resultado é: {divisao(x, y)}')
                break
            else:
                print('\nOperação inválida! Tente novamente') 
                
        except ValueError:
            print('\nErro: Por favor, digite apenas números válidos!')  
            
calc()