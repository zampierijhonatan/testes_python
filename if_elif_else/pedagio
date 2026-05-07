import os
os.system("cls")

def km():
    
    try:
        os.system("cls")
        percorrido = int(input("Digite a distância percorrida (em km): "))
        pedagio = 10
        
        
        if percorrido <= 100:
            print(f"\nValor do pedágio:{pedagio}\n")
        elif 100 < percorrido < 200:
            total = pedagio * 2
            print(f"\nValor do pedágio:{total}\n")
        else:
            total = pedagio * 3
            print(f"\nValor do pedágio:{total}\n")
            
    except:
        os.system("cls")
        input("Digite um km válido!! Digite algo para tentar novamente.")
        km()
        
km()