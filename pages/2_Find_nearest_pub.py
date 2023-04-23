import streamlit as st
import pandas as pd
import numpy as np
import os

st.title(':red[Find the nearest pubs]')

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

DATA_PATH = os.path.join(dir_of_interest, "data", "open_pubs_cleaned.csv")

df = pd.read_csv(DATA_PATH)

lat=st.number_input(label="Enter the Latitude", min_value=49.892485, max_value=60.764969)
lon=st.number_input(label="Enter the Longitude", min_value=-7.384525, max_value=1.757763)

def euc_dis(lat1,lon1,lat2,lon2):
    return np.sqrt((lat1-lat2)**2+(lon1-lon2)**2)

df['dist']=df.apply(lambda row: euc_dis(row['latitude'],row['longitude'],lat,lon),axis=1)
distance=df.sort_values(by='dist')[:5]
st.subheader('5 nearest pubs')
st.dataframe(distance)
st.map(data=distance)