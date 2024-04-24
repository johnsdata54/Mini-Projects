import requests
import streamlit as st
import pandas as pd

#URL object
url = "https://the-cocktail-db3.p.rapidapi.com/"

#API Keys/Insert your own from "Cocktail DB API" on Rapid Api to work
headers = {
	"X-RapidAPI-Key": '''place your API KEY HERE''',
	"X-RapidAPI-Host": "the-cocktail-db3.p.rapidapi.com"
}

#Response object
response = requests.get(url, headers = headers)

#Creating Dataframe that contains cocktail data
df = pd.DataFrame(response.json(), 
                  columns = ['id',  'title', 'difficulty', 'image'])

#Creates dropdown select bar for cocktail App in webpage
select = st.selectbox(label = "Select drink here", 
                      options = df.loc[:,'title'].to_list())

#Creating 2 columns in webpage layout
col1,col2 = st.columns(2)

#First column
with col1:
    #Name of drink
    st.header(select)
    
    #Setting index of the title to object
    index = df.index[df['title'] == select]

    #Concatenating the string version of the index object to the url
    url2 = "https://the-cocktail-db3.p.rapidapi.com/" + str(index[0]+1)
    
    #Setting second URL to second response object
    response2 = requests.get(url2, headers = headers)

    #Retrieving image from first URL and retrieving the caption form the second URL 
    st.image(image = response.json()[index[0]]['image'], 
             caption = response2.json()['description'])
    
#Second column
with col2:
    
    #Defining layout of the right column
    st.subheader(f"Difficulty:")

    #Displaying difficulty of the drink
    st.write(f"- {response.json()[index[0]]['difficulty']}")
    st.subheader(f"Ingredients:")
    
    #Based on selected item in the "select" object (line 23), gives the list of ingredients
    for i in response2.json()['ingredients']:
        st.write(f"- {i}")
    
#Step information section of layout       
st.write(f"Steps:")

#Based on selected item in the "select" object (line 23), gives the list of steps
for i in range(len(response2.json()['method'])):
        
        #Steps
        st.write(f"- Step {i+1} ")
        st.write(response2.json()['method'][i][f'Step {str(i+1)}'])
             
             
             




