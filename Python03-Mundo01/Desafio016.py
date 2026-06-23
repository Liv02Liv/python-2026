#%%
#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math 
num = float(input("Digite um valor: "))
print(f"O valor digitado foi {num} e a sua poção inteira é {math.trunc(num)}")