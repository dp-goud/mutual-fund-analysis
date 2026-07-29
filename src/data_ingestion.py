import pandas as pd
import os

path = "data/raw"

for file in os.listdir(path):
    if file.endswith(".csv"):

        df = pd.read_csv(os.path.join(path, file))

        print("=" * 50)
        print(file)
        print(df.shape)
        print(df.dtypes)
        print(df.head())
