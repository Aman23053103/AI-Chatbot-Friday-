import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="Your API KEY")  # <-- Replace with your actual key

model = genai.GenerativeModel('gemini-1.5-flash')

# Streamlit App UI
st.title("🤖 Friday")
user_input = st.text_input("Ask a question:")

if st.button("Ask Friday"):
    if user_input:
        response = model.generate_content(user_input)
        st.markdown("**Response:**")
        st.write(response.text)
