#%%
import pandas as pd 
from sqlalchemy import create_engine

engine = create_engine("sqlite:///Dados.db")

df = pd.read_csv("coffee_shop_sales.csv", sep=",")

df.to_sql("coffee", engine, if_exists = "replace", index = False)

#%%
import sqlite3
import pandas as pd

# Conecta ao banco existente
conexao = sqlite3.connect("Dados.db")

# Lê o arquivo CSV
df = pd.read_csv("marathon-data.csv")

# Cria a tabela e insere os dados
df.to_sql("marathon", conexao, if_exists="replace", index=False)

conexao.close()

print("Tabela marathon criada com sucesso!")

#%%
import sqlite3
import pandas as pd

# Conecta ao banco existente
conexao = sqlite3.connect("Dados.db")

# Lê o arquivo CSV
df = pd.read_csv("hotel_bookings.csv")

# Cria a tabela e insere os dados
df.to_sql("hotel", conexao, if_exists="replace", index=False)

conexao.close()

print("Tabela hotel criada com sucesso!")

#%%
import sqlite3
import pandas as pd

# Conecta ao banco existente
conexao = sqlite3.connect("Dados.db")

# Lê o arquivo CSV
df = pd.read_csv(r"pizza_sales\price_history.csv")

# Cria a tabela e insere os dados
df.to_sql("price_history", conexao, if_exists="replace", index=False)

conexao.close()

print("Tabela price_history criada com sucesso!")

#%%
import sqlite3
import pandas as pd

# Conecta ao banco existente
conexao = sqlite3.connect("Dados.db")

# Lê o arquivo CSV
df = pd.read_csv(r"pizza_sales\transactions.csv")

# Cria a tabela e insere os dados
df.to_sql("transactions", conexao, if_exists="replace", index=False)

conexao.close()

print("Tabela transactions criada com sucesso!")