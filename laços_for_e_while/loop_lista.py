import os
os.system("cls")


print("\n- - - - - - - - Loop n*1 - - - - - - - -\n")   
livros2 = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]

for livro2 in livros2:
    if livro2["estoque"] == 0:
        continue
    print(f"Livro encontrado: {livro2["nome"]}")
    
    
    
    
print("\n- - - - - - - - Loop n*2 - - - - - - - -\n")      
valores = [10, 20, 30, 40, 50]

soma = 0

for valor in valores:
    soma += valor
    
print(f"A soma total das receitas é: {soma}")
    
    
    
print("\n- - - - - - - - Loop n*3 - - - - - - - -\n")       
livros1 = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

for livro1 in livros1:
    if livro1 == "O Hobbit":
        print(f"Livro encontrado: {livro1}")
        break
print("\n")       