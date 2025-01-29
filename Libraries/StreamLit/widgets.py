import streamlit as st

st.title("streamlit Text input  ")
name  = st.text_input("Enter Your name :")

if name:
    st.write(f"Hello {name}")