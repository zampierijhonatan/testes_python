def temperatura():
    try:

        temp = float(input("\nDigite a temperatura atual: "))

        if temp <= 25:
            print("\nTemperatura dentro do normal!\n")
        else:
            print("\nAlerta! Temperatura acima  do limite permitido.\n")
          
    except:
        print("\nDigite uma temperatura válida\n")
        temperatura()
        
temperatura()