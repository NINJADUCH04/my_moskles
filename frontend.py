import streamlit as st
import requests

st.title('Welcome to mM!')

st.write('Tell me what kind of background do you need ? ')


user_input = st.text_input('Enter Description:', 'I love pizza !! ')

if user_input:
   try :
        response = requests.post(
                
                "http://127.0.0.1:8000/analyze-sentiment",
                
                json={"text": user_input}
            )

        if response.status_code == 200:
            
            st.write("Generated Background:")
            
            st.write(response.json())
   
        else:
       
            st.error(f"Error: {response.status_code} - {response.text}")
   
   except requests.exceptions.RequestException as e:
     
        st.error(f"Failed to connect to the backend: {e}")



