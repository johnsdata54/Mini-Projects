import streamlit as st
import pandas as pd


difficulty = st.sidebar.selectbox("Select your difficulty of questioning", ["Easy", "Medium", "Hard","Info Tab"])



if difficulty == "Info Tab":
    st.header("Data Used")
    st.write("Bank marketing data set:")
    st.write("https://www.kaggle.com/datasets/henriqueyamahata/bank-marketing")

    st.header("Preview of Data")
    st.dataframe("")

    st.header("Questions Used")
    st.write("The question used to analyze this data set is developed by chatgpt.")

if difficulty == "Easy":
    st.header("1. What is the distribution of age among the customers in the dataset?")
    st.header("2. What is the most common education level among the customers?")
    st.header("3. How many customers have subscribed to the term deposit?")
    st.header("4. What is the percentage of customers who have a housing loan?")
    st.header("5. Which job category has the highest number of customers?")
    st.header("6. What is the average balance in the customers' accounts?")
    st.header("7. What is the marital status of the majority of customers?")
    st.header("8. How many customers have a personal loan?")
    st.header("9. What is the most common contact communication type?")
    st.header("10. How many customers are there in the dataset?")
if difficulty == "Medium":
    st.write("Medium")

if difficulty == "Hard":
    st.write("Hard")


