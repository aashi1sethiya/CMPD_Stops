import pandas as pd
import altair as alt
import streamlit as st
import matplotlib.pyplot as plt

@st.cache_data
def load_data(csv):
    df = pd.read_csv(csv)
    return df

stops = load_data("Officer_Traffic_Stops.csv")
stops_count = stops.groupby('Month_of_Stop').size().reset_index(name='count')
stops_count = stops_count.sort_values(by="Month_of_Stop")

line_chart = (
    alt.Chart(stops_count).mark_line(point=True)
    .encode(
        x="Month_of_Stop:T",
        y="count:Q",
        tooltip=["Month_of_Stop", "count"],)
    .properties(
        width=600,  # Set width of the chart
        height=300,  # Set height of the chart
        title="Number of Stops per Month",
    )
)

st.altair_chart(line_chart, use_container_width=False, theme="streamlit")