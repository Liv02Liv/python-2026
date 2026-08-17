#%%
import pandas as pd

(
    pd.read_csv("employee_satisfaction_survey.csv", parse_dates=["Timestamp"])
    .sort_values("Timestamp")
    .groupby("Email").tail(1) ["Satisfaction"]
    .value_counts()
)
