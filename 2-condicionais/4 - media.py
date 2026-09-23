import os
os.system('cls')

nome = input('Digite seu nome: ')
idade = int(input('Digite Sua idade:'))
primeira_nota = float(input('Digite a primeira nota: '))
segunda_nota = float(input('Digite a Segunda Nota: '))

media = (primeira_nota + segunda_nota)

print('\n= EXIBINDO DADOS =')
print('nome: ', nome)
print('idade: ', idade)
print('primeira nota: ', primeira_nota)
print('segunda nota: ', segunda_nota)
print('Média: ', media)
