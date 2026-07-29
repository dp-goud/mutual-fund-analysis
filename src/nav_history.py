import pandas as pd
import os


raw_path = "data/raw"


files = [
    "hdfc_top100.csv",
    "sbi_bluechip.csv",
    "icici_bluechip.csv",
    "nippon_large_cap.csv",
    "axis_bluechip.csv",
    "kotak_bluechip.csv"
]


all_nav = []


for file in files:

    path = os.path.join(raw_path, file)

    df = pd.read_csv(path)

    all_nav.append(df)

    print(file, df.shape)


# combine all files

nav_history = pd.concat(all_nav, ignore_index=True)


print("\nFinal NAV History Shape:")
print(nav_history.shape)


print("\nColumns:")
print(nav_history.columns)


# save

nav_history.to_csv(
    "data/raw/nav_history.csv",
    index=False
)


print("\nnav_history.csv created successfully!")
