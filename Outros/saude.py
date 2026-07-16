#%%
# Alerta automático de febre
temperaturas = [36.5, 37.1, 38.4, 39.0]

for temp in temperaturas:
    if temp >= 38:
        print("Alerta de Febre")
    
    else:
        print("Temperatura Normal")

#%%
# Organização de exames 

exames = [120, 98, 140, 85]

for resultado in exames:
    if resultado > 100:
        print("Alterado")

    else:
        print("Normal")

#%%
# Identificação de pacientes prioritários 

idades = [22, 67, 81, 45]

for idade in idades:
    if idade >= 60:
        print("Prioritário")

    else:
        print("Atendimento comum")