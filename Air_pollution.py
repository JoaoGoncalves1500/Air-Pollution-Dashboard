import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import streamlit as st
import plotly.express as px

#Set the Web Page
st.set_page_config(page_title="Poluição Mundial",layout='wide')
st.title("Global Air Pollution")

# Load the dataset
df=pd.read_csv('air_pollution new.csv')
st.write(df)

# Menu Data
st.sidebar.header("Global Air pollution")

anos = ["2017","2018","2019","2020","2021","2022","2023"]
data = st.sidebar.multiselect("Select the year(s)",anos)
#check_2017 = st.sidebar.checkbox("2017")
#check_2018 = st.sidebar.checkbox("2018")

# Dashboard
#st.bar_chart(df["country"],df["2017"])