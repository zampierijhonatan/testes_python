def soma_recursiva(n):
    if n == 1:
        return 1
    return n + soma_recursiva(n - 1)


num = int(input('Digite um número: '))
print(f'A soma de 1 a {num} é: {soma_recursiva(num)}')

