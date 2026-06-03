import os

def age():
    while True:
        try:
            os.system('cls')
            atual = int(input("Em que ano estamos: "))
            nascimento = int(input("\nEm qual ano você nasceu: "))

            idade = atual - nascimento

            print(f"\nSua idade é: {idade} anos!")
            break
        except:
            os.system('cls')
            input("Digite um número válido, digite qualquer tecla para tentar novamente!")
            
            
age()