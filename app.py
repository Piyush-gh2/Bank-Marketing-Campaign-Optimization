import streamlit as st
import pandas as pd

st.title("Bank Marketing AIOps Dashboard")

df = pd.read_csv("../data/anomaly_output.csv")

st.subheader("Campaign Conversion Probability")
st.write(df["conversion_probability"].describe())

st.subheader("Anomaly Count")
st.write(df["anomaly_flag"].value_counts())

st.subheader("Top High-Probability Customers")
st.write(df.sort_values("conversion_probability", ascending=False).head(10))