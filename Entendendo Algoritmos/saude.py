#%%
# Alerta automático de febre
temperaturas = [36.5, 37.1, 38.4, 39.0]

for temp in temperaturas:
    if temp >= 38:
        print("Alerta de Febre")
    
    else:
        print("Temperatura Normal")