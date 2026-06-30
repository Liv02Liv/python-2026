#%%
#Crie um programa que leia um número Real qualquer pelo 
# teclado e mostre na tela a sua porção Inteira.
print("DESAFIO 016")

from math import trunc  
num = float(input("Digite um valor: "))
print(f"O valor digitado foi {num} e a sua poção inteira é {trunc(num)}")

#%%
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente 
#de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
print("DESAFIO 017")

co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f"A hipotenusa vai medir {hi:.2f}")

#%%
from math import hypot
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = hypot(co, ca)
print(f"A hipotenusa vai medir {hi:.2f}")

#%%
# Faça um programa que leia um ângulo qualquer e 
# mostre na tela o valor do seno, cosseno e tangente desse ângulo.
print("DESAFIO 018")

from math import radians, sin, cos, tan

angulo = float(input("Digite o ângulo que você deseja: "))

seno = sin(radians(angulo))
print(f"O ângulo de {angulo} tem o SENO de {seno:.2f}")

cosseno = cos(radians(angulo))
print(f"O ângulo de {angulo} tem o COSSENO de {cosseno:.2f}")

tangente = tan(radians(angulo))
print(f"O ângulo de {angulo} tem a TANGENTE de {tangente:.2}")

#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, 
# lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
#%%
print("DESAFIO 019")

from random import choice

n1 = str(input("Digite o primeiro nome: "))
n2 = str(input("Digite o sengudo nome: "))
n3 = str(input("Digite o terceiro nome: "))
n4 = str(input("Digite o quanto nome: "))

lista = [n1, n2, n3, n4]
sort = choice(lista)

print(f"O aluno escolhido foi {sort}")

#%%
#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
print("DESAFIO 020")

from random import shuffle

n1 = str(input("Primeiro aluno: "))
n2 = str(input("Segundo aluno: "))
n3 = str(input("Terceiro aluno: "))
n4 = str(input("Quarto aluno: "))

lista = [n1, n2, n3, n4]

shuffle(lista)

print(f"A ordem de apresentação será: {lista}")

#%%
#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
print("DESAFIO 021")

import pygame

pygame.init()
pygame.mixer.music.load("Victor Santos - Tenho Medo (Clipe Oficial) - Victor Santos (youtube).mp3")
pygame.mixer.music.play()
pygame.event.wait()