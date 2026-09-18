#LIMPAR O TERMINAL.
import os
os.system("cls")

#REGISTRO.

print("===== Registro de Eleição, Registre Seus Dados Abaixo =====")
digite_seu_nome_completo= input("Digite Seu Nome Completo: ")
idade= int(input("Digite Sua Idade: "))

#CÁLCULOS
if idade < 16:
    print("Não Pode Votar.")
elif idade >= 16 and idade <= 17:
    print("Voto Opcional.")
elif idade >= 18 and idade <= 65:
    print("Voto Obrigatório.")
else:
    print("Voto Não Obrigatório")

print('-'* 30)
print("Sessão Encerrada")
print('-'* 30)