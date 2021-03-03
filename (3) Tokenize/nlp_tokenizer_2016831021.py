import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize


def title_liner():
    for _ in range(150):
        print("-", end="")
    print("\n")
    return ""


data = pd.read_csv("../DataSets/prepared_data/data.csv")
bangla_data = data["Bangla"]

print(title_liner(), "Sentence Tokenize : \n", bangla_data.apply(sent_tokenize))

print(title_liner(), "Words Tokenize : \n", bangla_data.apply(word_tokenize))