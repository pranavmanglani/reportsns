import streamlit as st
import os

# --- Hardcoded credentials ---
USERNAME = "user"
PASSWORD = "pass123"

# --- Session state ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --- Login Page ---
def login():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
            st.success("Logged in successfully!")
        else:
            st.error("Invalid credentials")

# --- Upload & Manage PDFs ---
def pdf_dashboard():
    st.title("PDF Dashboard")

    # Upload Section
    uploaded = st.file_uploader("Upload a PDF", type=["pdf"])
    if uploaded:
        with open(uploaded.name, "wb") as f:
            f.write(uploaded.getbuffer())
        st.success(f"{uploaded.name} uploaded successfully!")

    # Display and manage PDFs
    st.subheader("Available PDFs")
    pdf_files = [f for f in os.listdir() if f.endswith(".pdf")]

    if not pdf_files:
        st.info("No PDFs available.")
    else:
        for pdf in pdf_files:
            col1, col2 = st.columns([4, 1])
            with col1:
                with open(pdf, "rb") as f:
                    st.download_button(
                        label=f"Download {pdf}",
                        data=f,
                        file_name=pdf,
                        mime="application/pdf",
                        key=f"download_{pdf}"
                    )
            with col2:
                if st.button("Delete", key=f"delete_{pdf}"):
                    os.remove(pdf)
                    st.success(f"{