import streamlit as st
import pandas as pd
import numpy as np
from numpy.random import default_rng as rng
import pydeck as pdk
import dotenv


dotenv.load_dotenv()

# load dataset and convert to dataframe
#df = pd.read_csv("C:/Users/User/Downloads/global climate data.csv")
 #refer to the row index:

#df.dropna(inplace= True)
#df.drop_duplicates(inplace=True)

website_title = st.title(body = "Balance Sheet Climate-Risk exposure",text_alignment= "center")

template = pdk.Deck(
        map_provider= "google_maps",
        map_style= "satellite",
        # Use Streamlit theme to pick map style
        initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,))

map = st.pydeck_chart(
    pydeck_obj = template,
    on_select = callable,
    selection_mode= "single-object",
    
)
