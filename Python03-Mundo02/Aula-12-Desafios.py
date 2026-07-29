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

#%%

#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais

print("DESAFIO 038")

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))

if n1 > n2:
    print("O PRIMEIRO valor é maior")
elif n2 > n1:
    print("O SEGUNDO valor é maior")
else:
    print("Os dois valores são IGUAIS")

#%%

#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, 
#de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
#se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

print("DESAFIO 039")

from datetime import date

atual = date.today().year
nasc = int(input("Ano de nascimento: "))
idade = atual - nasc

print(f"Quem nasceu em {nasc} tem {idade} anos em {atual}.")

if idade == 18:
    print("Você tem que se alistar IMEDIATAMENTE!")
elif idade < 18:
    saldo = 18 - idade 
    print(f"Ainda faltam {saldo} anos para o alistamento")
    ano = atual + saldo
    print(f"Seu alistamento será em {ano}")
elif idade > 18:
    saldo = idade - 18
    print(f"Você já deveria ter se alistado há {saldo} anos.")
    ano = atual - saldo 
    print(f"Seu alistamento foi em {ano}")