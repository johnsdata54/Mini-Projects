import streamlit as st
from faker import Faker
import numpy as np
import pandas as pd

fake = Faker()

#Data parameters
class Info():
    def __init__(self, email, name, number, address):
        self.email = email
        self.name = name
        self.number = number
        self.address = address

    def __iter__(self):
        return iter((self.email, self.name, self.number, self.address))

#Table that houses data
class Table():
    def __init__(self):
        self.table = []

    def append_data(self, info) -> list:
        self.table.append(info)

#Create dataframe
class Display():
    def __init__(self):
        self.df = pd.DataFrame(columns=['Email', 'Name', 'Number', 'Address'])
    def append_info(self,lst):
        new_df = pd.DataFrame([lst], columns=['Email', 'Name', 'Number', 'Address'])
        self.df = pd.concat([self.df, new_df], ignore_index=True)

# Create an instance of Display
display = Display()

#Option to download dataframe to csv, excel, sql

amount_of_people = st.number_input("Input of amount rows to generate")

count = 0

while count <= amount_of_people:
    count +=1
    personal_info = list(Info(
                email=fake.email(),
                name=fake.name(),
                number=fake.phone_number(),
                address=fake.address()  
    ))
    display.append_info(personal_info)

def generate_df():
    st.dataframe(display.df)

def download_df():
    st.download_button()

csv = pd.DataFrame.to_csv(display.df)

st.button("Press to Generate Dataframe", on_click=generate_df)

st.download_button(label="Download Data", 
                   data=csv,
                   file_name="streamlit_dataframe.csv",
                   mime="text/csv")