import streamlit as st
import pandas as pd
from PIL import Image

df=pd.read_csv('open_pubs_cleaned.csv')

st.title(':red[🍻Open Pub Application🍻]')
img=Image.open('pub.jpg')
st.image(img)

st.header(':blue[About the dataset]')

st.subheader('First five rows of the dataset')
st.write(df.head())

st.subheader('Shape of the dataset')
st.write('Rows :',df.shape[0])
st.write('Columns :',df.shape[1])

st.subheader('Total Count')
r1=st.radio('Select to see the total count',('Pubs','Local Authority','Postal Codes'))
if r1=='Pubs':
    st.write('The total number of Pubs in UK are 35809')
elif r1=='Local Authority':
    st.write('The total number of Local Authorities in UK are 360')
elif r1=='Postal Codes':
    st.write('The total number of Postal Codes in UK are 45230')
st.subheader('Basic Statistics of the dataset')
st.write(df.describe())