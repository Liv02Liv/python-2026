#%%
# API de medicamentos 

import requests

medicamento = "paracetamol"

url = f"URL_DA_API/{medicamento}"

dados = requests.get(url)

print(dados.json())