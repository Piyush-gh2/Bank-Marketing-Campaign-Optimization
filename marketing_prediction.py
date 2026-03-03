import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def train_model():
    df = pd.read_csv("data/processed_bank.csv")

    X = df.drop("y", axis=1)
    y = df["y"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    print(classification_report(y_test, predictions))

    df["conversion_probability"] = model.predict_proba(X)[:,1]
    df.to_csv("data/prediction_output.csv", index=False)

    return df

if __name__ == "__main__":
    train_model()