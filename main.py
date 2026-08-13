import streamlit as st
import pandas as pd
import numpy as np
from numpy.random import default_rng as rng
import pydeck as pdk
from dotenv import load_dotenv

load_dotenv()
# # load dataset and convert to dataframe
df = pd.read_csv("C:/Users/User/Downloads/global climate data.csv")
#  #refer to the row index:


df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

print(df.head())
drought_countries = df.groupby('drought_risk')
print(drought_countries.first())

website_title = st.title(body = "Balance Sheet Climate-Risk exposure",text_alignment= "center")



template = pdk.Deck(
        map_style= "dark",
        initial_view_state=pdk.ViewState(
            latitude=37.76,
            longitude=-122.4,
            zoom=11,
            pitch=50,
        ),
        
)


chart = st.pydeck_chart(
    pydeck_obj = template,
    selection_mode= "single-object")
