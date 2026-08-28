#LIMPAR O TERMINAL.
import os
os.system("CLS")

#PROCESSAMENTO.
print("===== FAÇA SEU CÁLCULOS ===== ")
primeiro_numero = float(input("Digite o Primeiro Número: "))
segundo_numero = float(input("Digite o Segundo Número: "))

#CÁLCULOS
soma = primeiro_numero + segundo_numero
media = soma /2
produto = primeiro_numero + segundo_numero

if  primeiro_numero > segundo_numero:
    maior = primeiro_numero
    menor = segundo_numero
else:
    maior = primeiro_numero
    menor = segundo_numero

#SAÍDA
print("\n===== RESULTADOS ===== ")
print(f":\nMédia: {media}")
print(f"\nSoma: {soma}")
print(f"\nProduto: {produto}")
print(f"\nMaior: {maior}")
print(f"\nMenor: {menor}")

#VERIFICANDO SÂO IGUAIS.
if primeiro_numero == segundo_numero:
    print("\nOs dois números informado são iguais. ")
else:
    print(f"\nMaior: {maior}")
    print(f"\nMenor: {menor}")
    
