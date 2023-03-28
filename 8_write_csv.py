import pandas as pd

#input
raw_data = pd.read_csv("Menu.csv")

#print(raw_data.info())

#process
total = raw_data["Price"].sum()

#output
print(f"Count:{len(raw_data.index)}")
print(raw_data)
print(f"Total:{total}")

raw_data.loc[len(raw_data)]=["total",total]

raw_data.to_csv("Menu_total.csv")
