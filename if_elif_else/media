import os
os.system("cls")

def final():
    while True:
        try:
                nota1 = float(input("Digite a primeira nota: "))
                nota2 = float(input("Digite a segunda nota: "))
                nota3 = float(input("Digite a terceira nota: "))
                
                if any(nota < 0 or nota > 10 for nota in[nota1, nota2, nota3]):
                    print("\nDigite uma nota válida!!\n")
                    input("Pressione qualquer tecla para tentar novamente!")
                    continue
            
                media = (nota1 + nota2 + nota3) / 3
                
                print(f"Sua média foi: {media:.2f}")
                
                if media >= 7 and media:
                    print("\nAprovado!!\n") 
                elif 5 <= media < 7 and media:
                    print("\nDe recuperação!!\n")
                else:
                    print("\nReprovado!!\n")
                    
                break
        except:
            os.system("cls")
            
            print("Digite um número válido!!\n")

final()