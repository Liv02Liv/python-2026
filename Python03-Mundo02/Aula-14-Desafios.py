#Nessa aula, vamos continuar a estudar os laços e vamos aprender 
#a usar a estrutura de repetição while no Python. Por exemplo:

#%%
# Usando o For

for c in range(1, 10):
    print(c)
print("Acabou!")

#%%
# Usando o while

c = 1

while c < 10:
    print(c)
    c = c + 1
print("Acabou!")

#%%

n = 1

while n != 0:
    n = int(input("Digite um valor: "))
    print(n)
print("Fim!")

#%%

n = 1
r = "S"

while r == "S":
    n = int(input("Digite um valor: "))
    r = str(input("Quer continuar? [S/N]")).upper()
    print(n)
print("Fim!")

#%%

n = 1
par = impar = 0

while n != 0:
    n = int(input("Digite um valor: "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
    print(n)

print(f"Você digitou {par} números pares e {impar} números ímpares!")

#%%

#Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, 
#mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

print("DESAFIO 057")

sexo = str(input("Informe seu sexo: [M/F] ")).strip().upper()[0]
while sexo not in "MnFf":
    sexo = str(input("Dados inválidos, por favor, informe seu sexo: ")).strip().upper()[0]
print(f"Sexo {sexo} registrado com sucesso!")

#%%

#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

print("DESAFIO 058")

from random import randint

computador = randint(0, 10)

print("Sou seu computador... Acabei de pensar em um número entre 0 e 10.")
print("Será que você consegue adivinhar qual foi? ")

acertou = False
palpites = 0

while not acertou:
    jogador = int(input("Qual é o seu Palpite? "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais... Tente mais uma vez.")
        elif jogador > computador:
            print("Menos.. Tente mais uma vez.")

print(f"Acertou com {palpites} tentativas. Parabéns!")