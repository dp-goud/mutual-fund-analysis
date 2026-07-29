import pandas as pd


fund_master = pd.read_csv(
    "data/raw/fund_master.csv"
)

nav_history = pd.read_csv(
    "data/raw/nav_history.csv"
)


# Convert to sets

fund_codes = set(fund_master["schemeCode"])

nav_codes = set(nav_history["schemeCode"])


print("Total Fund Master Schemes:")
print(len(fund_codes))


print("\nTotal NAV History Schemes:")
print(len(nav_codes))


# Check NAV schemes exist in fund master

invalid_codes = nav_codes - fund_codes


print("\nInvalid NAV Scheme Codes:")
print(len(invalid_codes))


if len(invalid_codes) == 0:
    print("All NAV scheme codes exist in fund master")
else:
    print(invalid_codes)


# Data Quality Summary

print("\nData Quality Summary")
print("--------------------")

print("Fund Master Schemes:", len(fund_codes))
print("NAV Schemes Loaded:", len(nav_codes))
print("Invalid Codes:", len(invalid_codes))
