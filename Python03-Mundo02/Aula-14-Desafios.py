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