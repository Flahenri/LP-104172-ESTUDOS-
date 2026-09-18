import os

# Llimpo o Terminal
os.system("cls")

# SOLICITANDO DADOS.
# input adicino o que for digitado no terminal no variável com texto.
nome = input('Digite seu nome: ')
sobrenome = input('Digite Seu Sobrenome: ')

# inp() converte o que foi digitado em inteiro (numeros inteiros)
idade = int(input('Digite sua idade: '))

# floot() converte o que foi digitado em floot (número_reais)
peso = float(input('Digite seu peso: '))
altura = int(input('Digite sua Altura: '))

# MOSTRANDO DADOS.
print('Nome: ', nome)
print('Sobrenome: ', sobrenome)
print('Idade: ', idade)
print('Peso: ', peso)
print('altura: ', altura)
