import streamlit as st
import pandas as pd
import plotly.express as px


#creating header with checkbox
st.header('Market of used cars.Original data')
st.write("""
##### Filter the data below to see the ads by manufacturer
""")

st.write("""
##### this is  a new message
""")
df = pd.read_csv('vehicles_us(1).csv')
df = df.drop(df.columns[0], axis=1)
manufacturer_choise = df['model'].unique()

st.selectbox('Select a model', manufacturer_choise)