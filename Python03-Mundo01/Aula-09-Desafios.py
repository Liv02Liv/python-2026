#%%
#Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

print("DESAFIO 022")

nome = str(input("Digite seu nome completo: ")).strip()

print("Analisando seu nome...")
print(f"Seu nome em maiúsculas é {nome.upper()}")
print(f"Seu nome em minúsculas é {nome.lower()}")
print(f"Seu nome tem ao todo {len(nome) - nome.count(' ')}")
print(f"Seu primeiro nome tem {nome.find(' ')} letras")

#%%
#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

print("DESAFIO 023")

numero = int(input("Digite um numero: "))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(f"Analisando o número {numero}")
print(f"Unidade: {unidade}")
print(f"Dezena: {dezena}")
print(f"Centena: {centena}")
print(f"Milhar: {milhar}")

#%%
#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

print("DESAFIO 024")

cidade = str(input("Em que cidade você nasceu? ")).strip()
print(cidade[:5].upper() == "SANTO")

#%%
#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

print("DESAFIO 025")

nome = str(input("Qual é seu nome completo? ")).strip()
print(f"Seu nome tem Silva? {"silva"in nome.lower()}")

#%%
#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
#em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

print("DESAFIO 026")

frase = str(input("Digite uma frase: ")).upper().strip()

print(f"A letra A aparece {frase.count("A")} vezes na frase.")
print(f"A primeira letra A apareceu na posição {frase.find("A")+1}")
print(f"A última letra A apareceu na posição {frase.rfind("A")+1}")

#%%
#

