import pandas as pd
import altair as alt
import streamlit as st
import matplotlib.pyplot as plt

@st.cache_data
def load_data(csv):
    df = pd.read_csv(csv)
    return df

stops = load_data("Officer_Traffic_Stops.csv")

stops['Driver_Age'].hist(bins=50, figsize=(8, 6))
plt.xlabel('Driver_Age', fontsize=14)
plt.ylabel('Frequency', fontsize=14)

st.pyplot()