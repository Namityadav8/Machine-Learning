import streamlit as st
import pandas as pd 
st.title("streamlit Text input  ")
name  = st.text_input("Enter Your name :")

if name:
    st.write(f"Hello {name}")


age =st.slider("Select your age :",0,100,25)
st.write(f"Age is {age}")

choice = ["python","Java","cpp","c#"]

options = st.selectbox("Chose your favourite Language ",choice)
st.write(f"Your favourite Language is {options}")


uploaded_file = st.file_uploader("choose your csv file ",type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    s.write(df) 