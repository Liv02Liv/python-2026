#%%
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///dados.db")

# Csv1 estoque 

df1 = pd.read_csv("VigiMed_Medicamentos.csv", sep=";")
df1.to_sql("medicamentos", engine, if_exists="replace", index=False)





