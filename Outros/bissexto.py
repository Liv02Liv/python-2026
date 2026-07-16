#%%
n = int(input())
is_leap = False

if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
    is_leap = True

if is_leap:
    print("Ano Bissexto")

else:
    print("Não é um Ano Bissexto")


#Verifique se um ano é bissexto ou não.