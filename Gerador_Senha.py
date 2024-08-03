#Gerador de senhas sem função (def)
import random

import string

# Recebe todas as letras do alfabeto em Maisculas
letras = string.ascii_uppercase

#variavel para caracteres especiais
sinais = '@#!$%&*()_-+='

# Recebe os numeros
numeros = '1234567890'

# Junção das 3 variaveis para ser usada em modo random
plus = letras + sinais + numeros

while True:

    tamanho_senha = int(input('Escolha o tamanho da sua senha: '))

    senha = ''.join(random.choice(plus) for c in range(tamanho_senha))
    print(f'Sua senha randomica é {senha}')

    if tamanho_senha <= 8:
        print('Sua senha é fraca')
    else:
        print('Sua senha é forte')

    continuar = input('Deseja continuar? [S/N] ').upper()
    if continuar == 'N':
        break