def vendas():

    try:
        maca = int(input("\nDigite quantas maçãs foram vendidas: "))
        bananas = int(input("\nDigite quantas bananas foram vendidas: "))
    
        if maca > bananas:
            print("\nAs maçãs tiveram mais vendas")
        elif maca == bananas:
            print("\nAs maçãs e as bananas venderam a mesma quantidade!!!\n")
        else:
            print("\nAs bananas tiveram mais vendas")
            
    except:
        print("Digite um número válido!\n")
        vendas()
        
        
vendas()        
        