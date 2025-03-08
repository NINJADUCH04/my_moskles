

import streamlit as st


st.title('Welcome to mM!')

st.write('Tell me what kind of background do you need ? ')


user_input = st.text_input('Enter Description:', 'I want sth pink ')
if user_input != 'I want sth pink ':
    st.write(user_input)



