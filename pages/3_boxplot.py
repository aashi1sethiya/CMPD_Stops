import pandas as pd
import altair as alt
import streamlit as st
import matplotlib.pyplot as plt

@st.cache_data
def load_data(csv):
    df = pd.read_csv(csv)
    return df

stops = load_data("Officer_Traffic_Stops.csv")

box = alt.Chart(stops).mark_boxplot().encode(
    x = alt.X('Was_a_Search_Conducted'),
    y = alt.Y('Driver_Age')
).properties(
    width = 500,
    title = 'Boxplot between Search Conducted vs Driver Age')

st.altair_chart(box)