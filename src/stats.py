import pandas as pd
import argparse

def count_labels(path):
    df = pd.read_csv(path)
    return df["final_label"].value_counts()


def paddy_ratio(path):
    counts = count_labels(path)    
    return counts["水田"]/ counts.sum() 




def paddy_ratio_by_region(path):
    df = pd.read_csv(path)
    df["is_paddy"] = df["final_label"] == "水田"

    return df.groupby("local_gove")["is_paddy"].mean()



def filter_by_confidence(path, threshold):
    df = pd.read_csv(path)
    return df[df["stage2_prob"] >= threshold]



def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("--threshold", type=float)

    args = parser.parse_args()


    if args.threshold is None:
      print(paddy_ratio_by_region(args.path))
    else:
      print(len(filter_by_confidence(args.path, args.threshold)))

if __name__ == "__main__":
    main()