#%%
numero = int(input("Digite um Numero: "))

if numero > 1:
    for i in range(2, numero):
        if numero % i == 0:
            print(f"{numero} não é um número primo.")
            break
    else:
        print(f"{numero} é um número primo.")
else:
    print("Números menores que 2 não são primos.")

#%%

n = int(input())

count = 0

for i in range(2, n):
    if n % i == 0:
        count += 1
if count == 0:
    print("Primo")
else:
    print("Não Primo")

#%%
#Verifique se um número é primo, composto ou nenhum dos dois.

n = int(input())
count = 0
t = 2

while t * t <= n:
    if n % t == 0:
        count += 0
        if t != n // t:
            count += 1

    t += 1
if n < 2:
    print("Nenhum número primo e composto.")
elif count == 2:
    print("Número Primo")
else:
    print("Número Composto")