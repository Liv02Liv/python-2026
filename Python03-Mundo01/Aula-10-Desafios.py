#%%
#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e 
#peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

print("DESAFIO 028")

from random import randint
from time import sleep

computador = randint(0, 5)
print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5, tente adivinhar...")
print("-=-" * 20)
jogador = int(input("Em que numero eu pensei? "))
print("PROCESSANDO...")
sleep(3)

if jogador == computador:
    print("PARABÉNS! Você conseguiu me vencer!")
else:
    print("GANHEI! Tente outra vez!")

#%%
#Escreva um programa que leia a velocidade de um carro. 
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.

print("DESAFIO 029")

velocidade = float(input("Qual é a velocidade atual do carro? "))

if velocidade > 80:
    print("MULTADO! Você excedeu o limite permitido que é de 80km/h")
    multa = (velocidade - 80) * 7
    print(f"Você deve pagar uma multa de R${multa:.2f}!")
else:
    print("Tenha um bom dia! Dirija com segurança!")

#%%
#Crie um programa que leia um número inteiro e mostre na tela se ele 
#é PAR ou ÍMPAR.

print("DESAFIO 030")

numero = int(input("Me diga um número qualquer: "))
resultado = numero % 2

if resultado == 0:
    print(f"O número {numero} é PAR")
else:
    print(f"O número {numero} é ÍMPAR")

#%%
#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens 
#de até 200Km e R$0,45 parta viagens mais longas.

print("DESAFIO 031")

distancia = float(input("Qual é a distância da sua viagem? "))
print(f"Você está prestes a começar uma viagem de {distancia}Km.")

if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45

print(f"E o preço da sua passagem será de R${preço}")

#%%
#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

print("DESAFIO 032")

from datetime import date

ano = int(input("Que ano quer analisar? Coloque 0 para analsar o ano atual: "))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é BISSEXTO")
else:
    print(f"O ano {ano} não é BISSEXTO")

#%%
#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print("DESAFIO 033")

a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))

menor = a 

if b < a and b < c:
    menor = b

if c < a and c < b:
    menor = c

maior = a 

if b > a and b > c:
    maior = b

if c > a and c > b:
    maior = c 

print(f"O menor valor digitado foi {menor}")
print(f"O maior valor digitado foi {maior}")

#%%
#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
#Para salários superiores a R$1621,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

print("DESAFIO 034")

salario = float(input("Qual é o salário do funcionário? R$"))

if salario <= 1621:
    novo = salario + (salario * 15 / 100)

else:
    novo = salario + (salario * 10 / 100)

print(f"Quem ganhava R${salario:.2f} passa a ganhar R${novo:.2f} agora.")

#%%
#Desenvolva um programa que leia o comprimento de três retas
#e diga ao usuário se elas podem ou não formar um triângulo.

print("DESAFIO 035")

print("-=-" * 20)
print("Analisador de Triângulos")
print("-=-" * 20)

r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima PODEM FORMAR triângulos!")

else:
    print("Os segmentos acima NÂO PODEM FOORMAR triângulos!") 
