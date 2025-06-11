import streamlit as st
import requests

st.title("Create New User")

email = st.text_input("Email")
password = st.text_input("Password", type="password")
role = st.selectbox("Role", ["engineering", "finance", "general", "hr",  "marketing"])

if st.button("Create User"):
    payload = {
        "email": email,
        "password": password,
        "role": role
    }
    response = requests.post("http://localhost:8000/create_user", json=payload)
    st.write(response.json())