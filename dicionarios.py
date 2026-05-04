# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

dados = {'Nome': 'Jhonatan', 'Idade': 22, 'Cidade': 'Amparo'}


# 2 - Utilizando o dicionário criado no item 1:
# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
# Adicione um campo de profissão para essa pessoa;
# Remova um item do dicionário.
print('\n-------------------------\n')
print(f'Idade = {dados['Idade']}')
print('\n-------------------------\n')
dados['Idade'] = 23
print(f'Idade alterada para {dados['Idade']}')
print('\n-------------------------\n')


dados['Profissão'] = 'Programador'
print(f"{dados['Profissão']}")
print('\n-------------------------\n')

del dados['Cidade']

for chave, valor in dados.items():
    print(f'- {chave}: {valor}')
print('\n-------------------------\n')

# 3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.

quadrados = {x: x**2 for x in range(1,11)}
print(f'{quadrados}')
print('\n-------------------------\n')

# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

exite_nome = 'Nome' in dados
print(f'A chave "Nome" existe?  -  {exite_nome}')
print('\n-------------------------\n')

exite_cidade = 'Cidade' in dados
print(f'A chave "Cidade" existe?  -  {exite_cidade}')
print('\n-------------------------\n')

# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

frase = 'Python é muito legal e Python é bem criativo e legal'

palavras = frase.split()

contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1
        
print(f'{contagem}')
print('\n-------------------------\n')