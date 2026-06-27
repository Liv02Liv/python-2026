#%%
import pandas as pd 
from sqlalchemy import create_engine

engine = create_engine("sqlite:///Dados.db")

df = pd.read_csv("coffee_shop_sales.csv", sep=",")

df.to_sql("coffee", engine, if_exists = "replace", index = False)

