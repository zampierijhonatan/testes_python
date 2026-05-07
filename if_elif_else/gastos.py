# limite mensal de 3000

import os

def gastos():
    try:
        os.system("cls")
        gastei = float(input("Digite o total de despesas do mês: "))
        
        if gastei > 3000:
            print(f"\nAtenção! Você ultrapassou o limite do orçamento.\n")
        else:
            print(f"\nDespesas controladas! Está dentro do orçamento.\n")
            
    except:

        os.system("cls")
        print("Digite um número válido!\n")
        gastos()
              
gastos()