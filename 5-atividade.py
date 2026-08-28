import os
os.system("cls")

usuario = input("Digite seu Nome: ")

numero1 = int(input("Digite o Primeiro Número: "))
numero2 = int(input("Digite o Segundo Número: "))
numero3 = int(input("Digite o Terceiro Número: "))

maior = max(numero1, numero2, numero3)
menor = min(numero1, numero2, numero3)

print(f"\nPrimeiro Número: {numero1}")
print(f"\nSegundo Número: {numero2}")
print(f"\nTerceiro Número: {numero3}")
print(f"\nO Maior Número é: {maior}")
print(f"O Menor Número é: {menor}")