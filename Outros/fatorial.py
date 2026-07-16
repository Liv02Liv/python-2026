#%%
n = int(input())
fact = 1

if n < 0:
    print("Entrada inválida")
elif n == 0:
    print("O fatorial é 1")
else:
    for i in range(1, n + 1):
        fact *= i
    print(fact)

#programa para calcular o fatorial de um número