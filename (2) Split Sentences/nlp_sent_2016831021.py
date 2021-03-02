import pandas as pd

data = pd.read_csv("../DataSets/prepared_data/data.csv")
bangla_data = data["Bangla"]

splited_bangla_data = bangla_data.apply(lambda x: x.split())

print(splited_bangla_data)
