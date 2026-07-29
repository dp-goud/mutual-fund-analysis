import requests
import pandas as pd


url = "https://api.mfapi.in/mf"


response = requests.get(url)

print(response.status_code)


data = response.json()


df = pd.DataFrame(data)


print(df.head())


df.to_csv(
    "data/raw/fund_master.csv",
    index=False
)


print("fund_master saved")
