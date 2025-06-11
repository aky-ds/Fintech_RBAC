import streamlit as st
import requests

st.title("FinSolve Internal AI Assistant")

if "role" not in st.session_state:
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        st.session_state["email"] = email
        st.session_state["password"] = password
        st.session_state["role"] = True
else:
    query = st.text_input("Ask a question:")
    if st.button("Submit"):
        payload = {
            "email": st.session_state["email"],
            "password": st.session_state["password"],
            "query": query
        }
        response = requests.post("http://localhost:8000/chat", json=payload)
        st.write(response.json().get("response"))