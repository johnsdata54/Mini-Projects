import streamlit as st
from faker import Faker
import numpy as np
import pandas as pd

fake = Faker()

class Info():
    def __init__(self, email, name, number, address):
        self.email = email
        self.name = name
        self.number = number
        self.address = address


class Table():
    def __init__(self):
        self.table = []

    def append_data(self, info):
        self.table.append(info)


class Dataframer():
    def __init__(self):
        self.df = 
amount_of_people = 10

for i in amount_of_people:
    personal_info = list(Info(
                    email=fake.email(),
                    name=fake.name(),
                    number=fake.phone_number,
                    address=fake.address()  
    ))


    Table.append_data(personal_info)