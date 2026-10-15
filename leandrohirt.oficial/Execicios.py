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

#%%

"""1 bilhão de segundos dá quase 32 anos. O datetime do Python soma um timedelta à data de nascimento e 
mostra o momento exato: quem nasceu em 1º de janeiro de 2000 chega lá em 9 de setembro de 2031, 
à 1h46 da madrugada. Troque pela sua data e descubra o seu."""

from datetime import datetime, timedelta

nascimento = datetime(2002, 6, 6)
print(nascimento + timedelta(
    seconds= 1_000_000_000))

vividos = datetime.now() - nascimento
print(vividos.total_seconds())