import pandas as pd


df = pd.read_csv(
    "data/raw/fund_master.csv"
)


print("Shape:")
print(df.shape)


print("\nUnique Scheme Codes:")
print(df['schemeCode'].nunique())


print("\nSample Scheme Names:")
print(df['schemeName'].head(10))


print("\nISIN Growth available:")
print(df['isinGrowth'].notnull().sum())


print("\nISIN Dividend available:")
print(df['isinDivReinvestment'].notnull().sum())