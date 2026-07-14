#%%
import pandas as pd

# Load data
transactions = (
    pd.read_csv("transactions.csv", parse_dates=["order_date"])
    .sort_values("order_date")
)

price_history = (
    pd.read_csv("price_history.csv", parse_dates=["effective_date"])
    .sort_values("effective_date")
)

transactions.head()

price_history.head()

pd.merge_asof(
    transactions,
    price_history,
    left_on="order_date",
    right_on="effective_date",
    by="pizza_id",
    direction="backward"
).assign(line_total = lambda x: x.price * x.quantity).line_total.sum()