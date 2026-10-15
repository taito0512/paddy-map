import pandas as pd

sample=pd.read_csv("data/sample.csv")
print(len(sample))
print(sample["final_label"].value_counts())