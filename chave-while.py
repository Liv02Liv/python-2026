#%%
def procure_pela_chave(caixa_principal): # pyright: ignore[reportMissingParameterType, reportUnknownParameterType]
    pilha = caixa_principal.crie_uma_pilha_para_buscar() # pyright: ignore[reportUnknownMemberType]
    
    while pilha:
        caixa = pilha.pop()

        for item in caixa:
            if item.e_uma_caixa():
                pilha.append(item)
            elif item.e_uma_caixa():
                print("Achei a chave!")
                return
            
#%%
def procure_pela_chave(caixa):
    for item in caixa:

        if item.e_uma_caixa():
            procure_pela_chave(item)
        elif item.e_uma_chave():
            print("Achei a chave!")
            return
        
#%%
def regressiva(i):
    print(i)
    regressiva(i-1)