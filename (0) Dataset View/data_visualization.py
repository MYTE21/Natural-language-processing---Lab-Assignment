import read_data_set as data_set
from tabulate import tabulate


def title_liner():
    for _ in range(150):
        print("-", end="")
    print("\n")
    return ""


data = data_set.data

print("(1) DataSet :\n", tabulate(data.head(), headers='keys', tablefmt='psql'), title_liner())
print("(2) Number of sentence ({}) :\n".format(data.count().sum()), data.count(), title_liner())
print("(3) Description of Dataset:\n", data.describe(), title_liner())
print("(4) Null Data Items:\n", data.isna().sum(), title_liner())

