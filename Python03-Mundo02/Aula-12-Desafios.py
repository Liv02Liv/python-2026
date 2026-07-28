#Nessa aula, vamos aprender como criar estruturas condicionais aninhadas, 
#usando os comandos if.. elif.. else em programas Python.

#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

#%%
print("DESAFIO 036")

casa = float(input("Valor da casa: R$"))
salario = float(input("Salário do comprador: R$"))
anos = int(input("Quantos anos de finacimento? "))

prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

print(f"Para pagar uma casa de R${casa} em {anos}", end=" ")
print(f"a prestação será de R${prestacao:.2f}")

if prestacao <= minimo:
    print("Empréstimo pode ser CONCEDIDO!")
else:
    print("Empréstimo NEGADO!")

#%%

#Exercício Python 37: Escreva um programa em Python que leia um número inteiro
#qualquer e peça para o usuário escolher qual será a base de conversão: 
#1 para binário, 2 para octal e 3 para hexadecimal.

print("DESAFIO 037")

num = int(input("Digite um número inteiro: "))

print('''Escolha uma das bases para conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL\n''')

opçao = int(input("Sua opção: "))

if opçao == 1:
    print(f"{num} convertido para BINÁRIO é igual a {bin(num)[2:]}")
elif opçao == 2:
    print(f"{num} convertido para OCTAL é igual a {oct(num)[2:]}")
elif opçao == 3:
    print(f"{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}")
else:
    print("Opção inválids, Tente novamente.")