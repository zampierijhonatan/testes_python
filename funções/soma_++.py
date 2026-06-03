def totalzao():
    while True:
        try:
            valores = input('Digite os valores das vendas: ').split()
            total = sum(map(float, valores))
            print(f'O valor total das vendas foi: {total:.2f}')
            break
        
        except:
            print('Erro! Digite um valor válido!')
        
totalzao()