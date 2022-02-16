#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Importing Packages

import pandas as pd
import numpy as np
import plotly.express as px
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected = "true")
import streamlit as st
from PIL import Image

df = pd.read_csv("NFLX.csv")

#logo = Image.open("https://assets.brand.microsites.netflix.io/assets/7dc497e2-4975-11ec-a9ce-066b49664af6_cm_1440w.jpg?v=5")
st.image("https://assets.brand.microsites.netflix.io/assets/7dc497e2-4975-11ec-a9ce-066b49664af6_cm_1440w.jpg?v=5")

st.title("Netflix Stock")
st.write("Netflix has become a very essential part of our lives and so we found interest in looking at the business and how it performs in the stock market")

Viz = st.sidebar.radio("Please Select a Preference:", ("Line Plot", "Table", "Both"))

selection = st.sidebar.selectbox("Please Select an Option:", ("Open", "High", "Low",
                        "Close", "Adj Close", "Volume", "All"))

#User Result:
if selection == "Open":
    df1 = df[["Date", "Open"]]
elif selection == "High":
   df1 = df[["Date", "High"]]
elif selection == "Low":
   df1 = df[["Date", "Low"]]
elif selection == "Close":
   df1 = df[["Date", "Close"]]
elif selection == "Adj Close":
   df1 = df[["Date", "Adj Close"]]
elif selection == "Volume":
   df1 = df[["Date", "Volume"]]
elif selection == "All":
    df1 = df

fig = px.line(df1, x="Date", y=df1.iloc[:, 1], title='Netflix Stock Over Time')

if Viz == "Line Plot":
    st.plotly_chart(fig, use_container_width=True)
if Viz == "Table":
    st.dataframe(df1)
if Viz == "Both":
    st.dataframe(df1)
    st.plotly_chart(fig, use_container_width=True)
