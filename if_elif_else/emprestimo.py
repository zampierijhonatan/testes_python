import os
os.system("cls")

def emprestimo():
    try:
        
        os.system("cls")
        renda = float(input("Digite o valor da sua renda mensal: "))
        parcela = float(input("Digite o valor da parcela desejada: "))
        
        porcento = renda * 0.3
        
        if porcento <= parcela:
            print(f"Emprestimo aceito! Valor da parcela: {porcento:.2f}")
        else:
            print(f"Emprestimo negado! Valor da parcela acima de 30%. Valor da parcela: {porcento:.2f}")
            
    except:
        os.system("cls")
        input("Número inválido! Aperte qualquer tecla para tentar novamente")
        emprestimo()
    
emprestimo()
