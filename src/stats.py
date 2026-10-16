import pandas as pd

def count_labels(path):
    df = pd.read_csv(path)
    return df["final_label"].value_counts()
print(count_labels("data/sample.csv"))

def paddy_ratio(path):
    counts = count_labels(path)    
    return counts["水田"]/ counts.sum() 

print(paddy_ratio("data/sample.csv"))


def paddy_ratio_by_region(path):
    df = pd.read_csv(path)
    df["is_paddy"] = df["final_label"] == "水田"

    return df.groupby("local_gove")["is_paddy"].mean()

print(paddy_ratio_by_region("data/sample.csv"))

def filter_by_confidence(path, threshold):
    df = pd.read_csv(path)
    return df[df["stage2_prob"] >= threshold]

print(len(filter_by_confidence("data/sample.csv", 0.3))) 