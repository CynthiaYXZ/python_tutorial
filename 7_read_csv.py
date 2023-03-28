import pandas as pd

#input
raw_data = pd.read_csv("Menu.csv")
print(raw_data)
print(raw_data.info())

#process
total = raw_data["Price"].sum()

#output
print(f"total:{total}")
