#%%
#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e 
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

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

distancia = float(input("Qual é a distância da sua viagem? "))
print(f"Você está prestes a começar uma viagem de {distancia}Km.")

if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45

print(f"E o preço da sua passagem será de R${preço}")