# Limpar o Terminal

import os
os.system('cls')

# Solicitar um número inteiro ao usuário
numero = int(input('digite o numero: '))

#calcula o antecessor e o sucessor
antecessor = numero - 1
sucessor = numero + 2

# Exibe os Resultados
print(f'O Antecessor de {numero} é {antecessor}. ')
print(f'O Sucessor de {numero} é {sucessor}. ')