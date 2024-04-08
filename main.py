import streamlit as st
import pandas as pd

st.write('CMPD Traffic Stops')
st.write('Lasya Edunuri was here!')

@st.cache_data
def load_data(csv):
    df = pd.read_csv(csv)
    return df

stops = load_data("Officer_Traffic_Stops.csv")

st.dataframe(stops)
