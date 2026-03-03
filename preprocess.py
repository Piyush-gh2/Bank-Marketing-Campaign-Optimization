import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess():
    df = pd.read_csv("data/bank.csv")

    # Encode categorical columns
    le = LabelEncoder()
    for col in df.select_dtypes(include='object').columns:
        df[col] = le.fit_transform(df[col])

    df.to_csv("data/processed_bank.csv", index=False)
    return df

if __name__ == "__main__":
    preprocess()