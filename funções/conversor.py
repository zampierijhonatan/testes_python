def converter_telefones(lista):
    return[int(telefone) for telefone in lista]

def verificar_tipos(lista):
    for num in lista:
        if not isinstance(num, int):
            return 'Erro na conversão'
    return 'Todos os números foram convertidos com sucesso!' 

telefones = ["11987654321", "21912345678", "31987654321", "11911223344"]    

telefones_convertidos = converter_telefones(telefones)

print(verificar_tipos(telefones_convertidos))

for tel in telefones:
    print(f'- {tel}')