import streamlit as st
import pandas as pd
import os

st.title(':red[Pub Locations]')

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

DATA_PATH = os.path.join(dir_of_interest, "data", "open_pubs_cleaned.csv")

df = pd.read_csv(DATA_PATH)

r1=st.radio('Search by',('Postal Code','Local Authority'))
if r1=='Postal Code':
    location=st.selectbox('Select the Postal Code',df['postcode'].unique())
    st.subheader(f"Total pubs found in the area are {df[df['postcode']==location].shape[0]}")
    st.map(data=df[df['postcode']==location])
elif r1=='Local Authority':
    location1=st.selectbox('Select the Local Authority',df['local_authority'].unique())
    st.subheader(f"Total pubs found in the area are {df[df['local_authority']==location1].shape[0]}")
    st.map(data=df[df['local_authority']==location1])