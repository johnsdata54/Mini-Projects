import streamlit as st
import pandas as pd

difficulty = st.sidebar.selectbox("Select your difficulty of questioning", ["Easy", "Medium", "Hard","Info Tab"])

if difficulty == "Info Tab":
    st.write("Info Tab")

if difficulty == "Easy":
    st.write("Easy")

if difficulty == "Medium":
    st.write("Medium")

if difficulty == "Hard":
    st.write("Hard")

st.write("test")

