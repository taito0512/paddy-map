import pandas as pd

def count_labels(path):
    df = pd.read_csv(path)
    return df["final_label"].value_counts()
print(count_labels("data/sample.csv"))