# Crie um programa que receba o peso (em kg) e a altura (em metros)

# calcule o IMC usando a fórmula: IMC = peso / (altura ** 2) 

# exiba o valor do IMC e uma mensagem indicando se está abaixo do peso (IMC < 18.5), peso normal (18.5 <= IMC < 25) ou acima do peso (IMC >= 25).
import os

def imc():
    try:

        os.system("cls")
        peso = float(input("\nDigite seu peso em kg: "))
        alt = float(input("\nDigite sua altura em metros: "))
        
        valor = peso / (alt ** 2)
        
        if valor < 18.5:
            print(f"\nSeu IMC é {valor:.2f}, você está abaixo do peso!\n")
        elif 18.5 <= valor < 25:
            print(f"\nSeu IMC é {valor:.2f}, seu peso está normal!\n")
        else:
            print(f"Seu IMC é {valor:.2f}, você está acima do peso!!")

    except:
        os.system("cls")
        print("\nDigite um número válido!")
        imc()
    
imc()