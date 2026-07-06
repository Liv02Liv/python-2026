#%%
import pandas as pd

coffee_df = pd.read_csv("coffee_shop_sales.csv", parse_dates=["date"])

coffee_df.head()

monthly_sales = (
coffee_df
.groupby(["store", coffee_df["date"].dt.month])
.agg({"sales": "sum"})
.reset_index()
.rename(columns={"date": "month"})
)

monthly_sales["sales_vs_last_month"] = monthly_sales.groupby("store")["sales"].diff()

monthly_sales.head(10)