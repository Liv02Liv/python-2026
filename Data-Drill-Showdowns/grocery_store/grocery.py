#%%
import pandas as pd
from itertools import combinations
from collections import Counter

grocery_df = pd.read_csv("grocery_transactions.csv")

grocery_df

#%%

tx_products = grocery_df.groupby("transaction_id") ["product_name"].apply(lambda x: sorted(set(x)))

tx_products

#%%

pair_counts = Counter()

for products in tx_products:
    if len(products) >= 2:
        for pair in combinations(products, 2):
            pair_counts[pair] += 1

pair_counts.most_common(5)