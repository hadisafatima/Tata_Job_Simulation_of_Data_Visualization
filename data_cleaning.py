import pandas as pd

file_path = r"C:\Users\HP\Downloads\Online Retail Data Set.xlsx"
data = pd.read_excel(file_path)

# print("Original Data: ")
# print(data.head(50))

# print("\n\nBefore clenaing data:")
# print(data.iloc[237])

data_cleaned = data[(data["Quantity"] >= 1) & (data["UnitPrice"] >= 0)]

# print("\n\nCleaned Data: ")
# print(data.head(50))

# print("\n\nChecking if data is cleaned?")
# print(data_cleaned.iloc[237])

data_cleaned.to_excel("Cleaned Online Retail Data Set.xlsx", index = False)

data_cleaned.info()