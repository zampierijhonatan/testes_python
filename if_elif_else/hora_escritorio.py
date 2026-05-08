

import os
os.system("cls")

def escritorio():
    try:
        hora = int(input("\nDigite a hora atual (formato 24 horas): "))
        
        if 8 <= hora < 18:
            print("\nAcesso liberado! Seja bem vindo/a!!\n")
        else:
            print("\nAcesso negado!\n")        
        
    except:
        os.system("cls")
        print("\nDigite um horário válido!!\n")
        escritorio()
        
escritorio()