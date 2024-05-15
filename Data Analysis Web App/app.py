import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("bank-additional-full.csv", delimiter=";")

difficulty = st.sidebar.selectbox("Select your difficulty of questioning", ["Easy", "Medium", "Hard","Info Tab"])



if difficulty == "Info Tab":
    st.header("Data Used")
    st.write("Bank marketing data set:")
    st.write("https://www.kaggle.com/datasets/henriqueyamahata/bank-marketing")

    st.header("Preview of Data")
    st.dataframe(df.head(10))

    st.header("Questions Used")
    st.write("The question used to analyze this data set is developed by chatgpt.")

if difficulty == "Easy":
    st.header("1. What is the distribution of age among the customers in the dataset?")

    arr = df['age']
    fig, ax = plt.subplots()
    ax.hist(arr, bins=10)

    st.pyplot(fig)

    st.header("2. What is the most common education level among the customers?")

    st.write(f"{df['education'].value_counts().idxmax()}")

    st.header("3. How many customers have subscribed to the term deposit?")

    st.write(f"The number of customers that have term deposits: {df['y'].value_counts()['yes']}")

    st.header("4. What is the percentage of customers who have a housing loan?")

    st.write(f"The number of personal loans taken: {round((df['housing'].value_counts()['yes']/df.shape[0])*100,2)} %")
    st.header("5. Which job category has the highest number of customers?")

    st.write(f"{df['job'].value_counts().idxmax()}")

    st.header("6. What is the average age in the customers' accounts?")

    st.write(f"The average age for a customer is: {round(df['age'].agg(['mean'])[0])}")

    st.header("7. What is the marital status of the majority of customers?")

    st.write(f"{df['marital'].value_counts().idxmax()}")

    st.header("8. How many customers have a personal loan?")

    st.write(f"The number of personal loans taken: {df['loan'].value_counts()['yes']}")
    st.write(f"The number of personal loans not taken: {df['loan'].value_counts()['no']}")
    st.write(f"The number of personal loans with an unknown status: {df['loan'].value_counts()['unknown']}")

    st.header("9. What is the most common contact communication type?")

    st.write(f"{df['contact'].value_counts().idxmax()}")

    st.header("10. How many customers are there in the dataset?")

    st.write(f"{df.shape[0]}")

if difficulty == "Medium":
    st.write("Medium")

if difficulty == "Hard":
    st.write("Hard")


