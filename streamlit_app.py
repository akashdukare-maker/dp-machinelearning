import streamlit as st
import pandas as pd

st.title('🤖 Machine Learning App')

st.info('This is Apps Builds a Mchine Learning Model')

with st.expander('Data'):
  st.Write('**Raw data**')
  df=pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
