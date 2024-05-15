import streamlit as st
import pandas as pd


difficulty = st.sidebar.selectbox("Select your difficulty of questioning", ["Easy", "Medium", "Hard","Info Tab"])



if difficulty == "Info Tab":
    st.header("Data Used")
    st.write("Bank marketing data set:")
    st.write("https://www.kaggle.com/datasets/henriqueyamahata/bank-marketing")

    st.header("Questions Used")
    st.write("The question used to analyze this data set is developed by chatgpt.")

if difficulty == "Easy":
    st.write("Easy")

if difficulty == "Medium":
    st.write("Medium")

if difficulty == "Hard":
    st.write("Hard")


