import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_extras.stylable_container import stylable_container


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
    st.write("What is the average duration of the last contact in seconds for customers who subscribed to the term deposit compared to those who didn't")

    yes_df = df[df['y'] == 'yes']
    no_df = df[df['y'] == 'no']

    st.write(f"The average duration of the last contact in seconds for customers who subscribe to the term deposit: {round(yes_df['duration'].agg(['mean'][0]),2)} seconds")
    st.write(f"The average duration of the last contact in seconds for customers who did not subscribe to the term deposit: {round(no_df['duration'].agg(['mean'][0]),2)} seconds")

    st.write("Is there any correlation between age and duration of the last contact?")

    correlation_data = df['age'].corr(df['duration'])

    st.scatter_chart(data=df,x='age', y='duration')

    with stylable_container(
        key="container_with_border",
        css_styles="""
            {
                border: 1px solid rgba(49, 51, 63, 0.2);
                border-radius: 0.5rem;
                padding: calc(1em - 1px)
            }
            """,
    ):
        st.markdown(f"The correlation between {round(correlation_data, 4)}.")

    st.write("What is the distribution of campaign contacts (number of contacts performed during this campaign) among customers who subscribed to the term deposit?")

    contact_counts = yes_df['campaign'].value_counts().sort_index()

    # Create the bar chart
    fig, ax = plt.subplots()
    ax.bar(contact_counts.index, contact_counts.values)
    ax.set_xlabel('Number of Contacts')
    ax.set_ylabel('Number of Customers')
    ax.set_title('Distribution of Campaign Contacts Among Customers Who Subscribed to the Term Deposit')

    # Display the chart in Streamlit
    st.pyplot(fig)


    st.write("Which marital status category has the highest proportion of customers who subscribed to the term deposit?")

    





    st.write("Are there any differences in the campaign success rate between different education levels?")

if difficulty == "Hard":
    st.write("Hard")


