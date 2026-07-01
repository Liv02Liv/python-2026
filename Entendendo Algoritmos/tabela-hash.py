#%%
caderno = dict()

caderno["maçã"] = 0.67
caderno["Leite"] = 1.49
caderno["abacate"] = 1.49

print(caderno)

#%%

voted = {} 

def verifica_eleitor(nome):
    if voted.get(nome):
        print("Mande embora!")
    else:
        voted[nome] = True
        print("Deixe votar") 

verifica_eleitor("tom")
verifica_eleitor("mike")
verifica_eleitor("mike")

#%%

cache = {}

def pega_pagina(url):
    if cache.get(url):
        return cache[url]
    else:
        dados = pega_dados_do_servidor(url)
        cache[url] = dados
        return dados
