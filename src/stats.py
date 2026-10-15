import pandas as pd

def count_labels(path):
    df = pd.read_csv(path)
    return df["final_label"].value_counts()
print(count_labels("data/sample.csv"))

def paddy_ratio(path):
    counts = count_labels(path)    
    return counts["水田"]/ counts.sum() 

print(paddy_ratio("data/sample.csv"))