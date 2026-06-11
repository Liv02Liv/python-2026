#%%
# API de medicamentos 

import requests
import json

medicamento = "ibuprofen"

url = (
    "https://api.fda.gov/drug/label.json"
    f"?search=openfda.generic_name:{medicamento}&limit=1"
)

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    print(json.dumps(dados, indent=4))
else:
    print(response.text)

