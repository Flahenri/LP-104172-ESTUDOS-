import os

os.system('cls')

print('SOLICITANDO DADOS =')
valor = float(input('digite o valor: '))
desconto = valor * 0.10
valor_com_desconto = valor - desconto

print('\n EXIBINDO DADOS =')
print('valor com desconto de 10%: ', valor_com_desconto)