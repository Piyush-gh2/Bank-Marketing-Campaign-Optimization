import pandas as pd

def generate_alerts():
    df = pd.read_csv("data/anomaly_output.csv")

    low_campaign = df[df["anomaly_flag"] == -1]

    for _, row in low_campaign.iterrows():
        print(f"🚨 ALERT: Campaign anomaly detected for customer ID {row.name}")

    return low_campaign

if __name__ == "__main__":
    generate_alerts()