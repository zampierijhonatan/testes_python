def criar_porcentagem(porcentagem):
    def criar_desconto(valor):
        return valor - (valor * (porcentagem / 100))
    return criar_desconto

desconto = float(input('Digite o valor do desconto: '))

preco_final = criar_porcentagem(desconto)

valor = float(input('Digite o valor da compra: '))

print(f'Preço final com desconto: {preco_final(valor)}')
