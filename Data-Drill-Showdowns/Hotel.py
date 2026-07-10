#%%
import pandas as pd

df = pd.read_csv("hotel_bookings.csv", parse_dates= ["checkin_date", "checkout_date"])
df.head()

df.dtypes

df.is_canceled.value_counts()

df = df[df.is_canceled == 0]
df.head()

df["night"] = [pd.date_range(ci, co, inclusive= "left") for ci, co in zip(df.checkin_date, df.checkout_date)]
df.head()

df_night = df.explode("night")
df_night.head()

df_month = df_night.night.dt.to_period("M").value_counts().sort_index().to_frame("booked_nights")
df_month.head()

df_month["available_nights"] = df_month.index.days_in_month * 200
df_month.head()

df_month["occ_rate"] = df_month.booked_nights / df_month.available_nights * 100
df_month.head()

df_month[df_month.index == "2016-07"]