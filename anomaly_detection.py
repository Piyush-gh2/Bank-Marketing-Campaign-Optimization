import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies():
    df = pd.read_csv("data/prediction_output.csv")

    model = IsolationForest(contamination=0.05)
    df["anomaly_flag"] = model.fit_predict(
        df[["conversion_probability"]]
    )

    df.to_csv("data/anomaly_output.csv", index=False)
    return df

if __name__ == "__main__":
    detect_anomalies()