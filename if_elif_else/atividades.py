import os

def atividades():
    try:
        os.system("cls")
        atia = int(input("Informe os dias para a atividade A: "))
        atib = int(input("Informe os dias para a atividade B: "))
        atic = int(input("Informe os dias para a atividade C: "))
        
        total = atia + atib + atic
        
        if atia <= 2:
            print(f"\nO tempo total para realizar as atividades é de {total}\n")
            print(f"Cuidado! Está chegando ao final do prazo da atividade A, você tem apenas {atia} dias!\n")
        elif atib <= 2:
            print(f"\nO tempo total para realizar as atividades é de {total}\n")
            print(f"Cuidado! Está chegando ao final do prazo da atividade A, você tem apenas {atib}dias!\n")
        elif atic <= 2:
            print(f"\nO tempo total para realizar as atividades é de {total}\n")
            print(f"Cuidado! Está chegando ao final do prazo da atividade A, você tem apenas {atic}dias!\n")
        elif atia <= 2 and atib <=2 and atic <=2:
            print("\nCUIDADO!!! Seu prazo para realizar as atividades está extremamente curto, agilize-as o mais rápido possível!\n")
            print(f"O tempo total para realizar as atividades é de {total}\n")
        else:
            print(f"\nO tempo total para realizar as atividades é de {total}\n")
            
    except:
        os.system("cls")
        print("\nDigite um número válido!!\n")
        atividades()
        
        
atividades()
        