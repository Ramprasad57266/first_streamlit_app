import streamlit

streamlit.title('My family new healthy diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 and Oatmeal')
streamlit.text('🥗Kale,Spinach & Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)

#New section to display fruitvice api response

streamlit.header("Fruityvice Fruit Advice!")

import requests
fruitvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruitvice_response.json())

