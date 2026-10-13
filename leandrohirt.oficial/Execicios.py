"""for i in len(nomes) dá TypeError porque o len devolve só a quantidade, 
um número, e o for precisa de algo com itens para percorrer. 
Passe a própria lista (for nome in nomes) ou, se precisar da posição, use range(len(nomes))."""

#%%
nomes = ["Ana", "Bia", "Caio"]
for nome in nomes:
    print(nome)

#%%
nomes = ["Ana", "Bia", "Caio"]
for i in range(len(nomes)):
    print(i, nomes[i])