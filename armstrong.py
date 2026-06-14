#%%
n = int(input())
s = 0
t = n 

while n > 0:
    digito = n % 10
    s += digito ** 3
    n //= 10

if s == t:
    print("Armstrong")

else:
    print("Não Armstrong")


#Verifique se um número é um número de Armstrong.