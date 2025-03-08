import streamlit as st
from model import analyze

st.title('Welcome to mM!')

st.write('Tell me what kind of background do you need ? ')


user_input = st.text_input('Enter Description:', 'I love pizza !! ')
if user_input != 'I love pizza !! ':
    st.write(analyze(user_input))



