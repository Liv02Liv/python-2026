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

#%%

#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, 
# mostrando uma mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO

print("DESAFIO 040")

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = (nota1 + nota2) / 2

print(f"Tirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {media:.1f}")

if 7 > media >= 5:
    print("O aluno está em RECUPERAÇÃO")
elif media < 5:
    print("O aluno está REPROVADO")
elif media >= 7:
    print("O aluno está APROVADO")

#%%

#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de 
#nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER

print("DESAFIO 041")

from datetime import date

atual = date.today().year
nascimento = int(input("Ano de nascimento: "))
idade = atual - nascimento

print(f"O atleta tem {idade} anos.")

if idade <= 9:
    print("Classificação: MIRIM")
elif idade <= 14:
    print("Classificação: INFANTIL")
elif idade <= 19:
    print("Classificação: JUNIOR")
elif idade <= 25:
    print("Classificação: SÊNIOR")
else:
    print("Classificação: MASTER")

#%%

#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando 
#o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

print("DESAFIO 042")

r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima PODEM FORMAR um triângulo", end=" ")
    if r1 == r2 == r3:
        print("EQUILÁTERO!")
    elif r1 != r2 != r3 != r1:
        print("ESCALENO!")
    else:
        print("ISÓSCELES!")
else:
    print("Os segmentos acima NÃO PODEM FORMAR triângulo")

#%%

#Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
#calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida

print("DESAFIO 043")

peso = float(input("Qual é seu peso? (Kg) "))
altura = float(input("Qual é a sua altura? (M) "))
imc = peso / (altura ** 2)

print(f"O IMC dessa pessoa é de {imc:.1f}")

if imc < 18.5:
    print("Você está ABAIXO DO PESO normal")
elif 18.5 <= imc < 25:
    print("PARABÉNS, você está na faixa de PESO NORMAL")
elif 25 <= imc < 30:
    print("Você está em SOBREPESO")
elif 30 <= imc < 40:
    print("Você está em OBESIDADE")
elif imc >= 40:
    print("Você está em OBESIDADE MÓRBIDA, Cuidado!")

#%%

#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros

print("DESAFIO 044\n")

print("{:=^40}".format(" LOJAS GUANABARA "))

preço = float(input("Preço das compras: R$"))

print("""FORMAS DE PAGAMENTOS
[1] à vista dinheiro|cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão""") 

opçao = int(input("Qual é a opção? "))

if opçao == 1:
    total = preço - (preço * 10 / 100)
elif opçao == 2:
    total = preço - (preço * 5 / 100)
elif opçao == 3:
    total = preço
    parcela = total / 2
    print(f"Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS")
elif opçao == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input("Quantas parcelas? "))
    parcela = total / totparc
    print(f"Sua compra será parcelada em {totparc:.2f} de R${parcela:.2f} COM JUROS")
else:
    total = preço
    print("OPÇÃO INVÁLIDA de pagamento, tente novamente!")

print(f"Sua compra de R${preço:.2f} vai custar R${total:.2f} no final.")


#%%

#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

print("DESAFIO 045\n")