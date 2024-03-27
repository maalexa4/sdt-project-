import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

#creating header with checkbox
st.header('Market of used cars.Original data')
st.write("""
##### Filter the data below to see the ads by manufacturer
""")


df = pd.read_csv('vehicles_us (1).csv')

df = df.drop(df.columns[0], axis=1)
manufacturer_choise = df['model'].unique()

selected_menu = st.selectbox('Select a model', manufacturer_choise )

min_year, max_year = int(df['model_year'].min()), int(df['model_year'].max())


year_range = st.slider("choose years", value=(min_year, max_year), min_value=min_year,max_value= max_year)



actual_range = list(range(year_range[0], year_range[1]+1))

df_filtered = df[ (df.model == selected_menu) & (df.model_year.isin(list(actual_range)) )]

df_filtered


st.header('Price analysis')
st.write("""
###### Let's analyze what influences price the most. We will check how distribution of price varies depending on transmission, fuel or type and condition
""")

list_for_hist = ('transmission','fuel','type','condition')

selected_type = st.selectbox('Split for price distribution',list_for_hist)

fig1 = px.histogram(df, x="model",color = selected_type )
fig1.update_layout(title= "<b> Split of price by {}</b>".format(selected_type))

st.plotly_chart(fig1)


def age_category(x):
    if x<5: return '<5'
    elif  x>=5 and x<10: return '5-10'
    elif x>=10 and x<20: return '10-20'
    else: return '>20'
df['age'] = 2024 - df['model_year']

df['age_category'] = df['age'].apply(age_category)

list_for_scatter = ['odometer','cylinders','paint_color']

choice_for_scatter = st.selectbox('Price dependency on',list_for_scatter)

fig2 = px.scatter(df, x="model", y=choice_for_scatter, color ="age_category",hover_data=['model_year'])
fig2.update_layout(title="<b> Model vs {}</b>".format(choice_for_scatter))
st.plotly_chart(fig2)

df['is_4wd'] = df['is_4wd'].fillna(0).astype(bool)

df['paint_color'] = df['paint_color'].fillna('unknown')