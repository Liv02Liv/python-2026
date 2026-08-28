#%%
#Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o “for”, 
#que é uma estrutura versátil e simples de entender. Por exemplo:

#for c in range(0, 4):

#print(c)

#print(‘Acabou’)

#%%

#Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para 
#o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

print("DESAFIO 046")

from time import sleep

for cont in range(10, -1, -1):
    print(cont)
    sleep(0.5)
print("BUM ! BUM! POOOW!")

#%%

#Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

print("DESAFIO 047")

for n in range(2, 51, 2):
    print(n, end=" ")
print("\nAcabou!")


#%%

#Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três
#e que se encontram no intervalo de 1 até 500.

print("DESAFIO 048")

soma = 0
cont = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c 
        cont += 1
print(f"A soma de todos os {cont} valores solicitados é {soma}")

#%%

#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, 
#só que agora utilizando um laço for.

