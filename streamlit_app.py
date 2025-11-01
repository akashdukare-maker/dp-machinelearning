import streamlit as st
import pandas as pd

st.title('🤖 Machine Learning App')

st.info('This is Apps Builds a Mchine Learning Model')

with st.expander('Data'):
   st.write('**Raw data**')
   df=pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
   df

st.write('**x**')
x=df.drop('species',axis=1)
x

st.write('**y**')
y=df.species
y

with st.expander('Data visualization'):
   st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')

with st.sidebar:
   st.header('Input features')
"bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g"
island=st.selectbox('island',('Biscoe','Dream','Torgersen'))
gender=st.selectbox('Gender',('male','female'))
bill_length_mm=st.slider('Bill length (mm)', 32.1,59.6,43.9)
