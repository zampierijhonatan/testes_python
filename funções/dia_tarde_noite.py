def dia_tarde_noite():
    
    while True:
        try:
            
            horas = int(input("Em que horas está acessando o app(24h): "))
            
            if 0 <= horas <=23:
                
                if horas < 12:
                    print("Bom dia!")
                elif 12 <= horas < 18:
                    print("Boa tarde!")
                else:
                    print("Boa noite!")
                    break
            else:
                print("Hora invalida! digite um numero entre o 0 e 23")
        except:
            input("Digite uma hora válida!")


dia_tarde_noite()
                
            