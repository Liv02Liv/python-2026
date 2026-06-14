#%%
# Modo Junio 
n = int(input("Digite um Numúro: "))
rev = 0
temp = n 

while temp > 0:
    digito = temp % 10
    rev = rev * 10 + digito
    temp = temp // 10
if n == rev:
    print("Palíndromo")
else:
    print("Não Palíndromo")

#%%
# Modo Senior
n = int(input("Digite um Numúro: "))
rev = int(str(n)[::-1])
if n == rev:
    print("Palíndromo")
else:
    print("Não Palíndromo")

