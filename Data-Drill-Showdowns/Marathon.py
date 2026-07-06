#%%
import pandas as pd

marathon_df = pd.read_csv("marathon-data.csv")
marathon_df.head()

marathon_df["final_minutes"] = pd.to_timedelta(marathon_df.final).dt.total_seconds() / 60

band_edges = [0, 180, 210, 240, 270, 300, 330, 360, float("inf")]
band_labels = ["sub 3", "3-3:30", "3:30-4", "4-4:30", "4:30-5", "5-5:30", "5:30-6", "6+"]

marathon_df["band"] = pd.cut(
    marathon_df.final_minutes,
    bins = band_edges,
    labels = band_labels,
    right= False
)

marathon_df.band.value_counts(normalize = True)