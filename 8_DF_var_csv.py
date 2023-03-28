import pandas as pd

#input
raw_data = pd.read_csv("Menu.csv")
print(raw_data)
#print(raw_data.info())

#process
total = raw_data["Price"].sum()
var = raw_data["Price"].var()
std = raw_data["Price"].std()
sorted = raw_data["Price"].sort_values()
Pricesorted = raw_data.sort_values("Price")
Pricesorted = raw_data.sort_values("Price", ascending=False)
#output
print(f"VAR:{var}")
print(f"STD:{std}")
print(sorted)
print(Pricesorted)