contador = 1

print("\n")
print("\n- - - - - - - - Loop n*1 - - - - - - - -\n")
print("\n")
while contador < 11:
    print(f"Processando dados...{contador}")
    contador += 1


print("\n")
print("\n- - - - - - - - Loop n*2 - - - - - - - -\n")
print("\n")
for i in range(5):
    print("Bem-vindo ao Buscante")
    

print("\n")
print("\n- - - - - - - - Loop n*3 - - - - - - - -\n")
print("\n")
projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for projeto in projetos:
    if projeto is None:
        print("Projeto ausente")
    else:
        print(projeto)


print("\n")    
print("\n- - - - - - - - Loop n*4 - - - - - - - -\n") 
print("\n")   
estoque = 5

while estoque > 0:
    print(f"Venda realizada! Estoque restante: {estoque}")
    estoque -= 1

print("Estoque esgotado")


print("\n")
print("\n- - - - - - - - Loop n*5 - - - - - - - -\n")
print("\n")
segundos = 10

while segundos > 0:
    if segundos % 2 == 0:
        print(f"\nFaltam apenas {segundos} segundos - Não perca essa oportunidade!\n")
    else:
        print(f"\nA contagem continua: {segundos} segundos restantes.\n")
    segundos -= 1
    
print("\nAproveite a promoção agora!")

  
print("\n")   
print("\n- - - - - - - - Loop n*6 - - - - - - - -\n")
print("\n")
while True:
    user = input("Digite seu nome de usuario: ")
    senha = input("Digite sua senha: ")

    if len(user) < 5:
        print("\n nome de usuario deve conter ao menos 5 caracteres!\n")
        continue
    
    if len(senha) < 8:
        print("\nA senha deve conter ao menos 8 caracteres!\n")
        continue
    
    print("\nCadastro realizado com sucesso!")
    break