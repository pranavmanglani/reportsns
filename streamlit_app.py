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
        if username == "admin" and password == "pass":
            st.session_state.logged_in = True
            st.success("Logged in successfully!")
        else:
            st.error("Invalid credentials")

# --- Upload & Download Dashboard ---
def pdf_dashboard():
    st.title("PDF Dashboard")

    # Upload PDF
    uploaded = st.file_uploader("Upload a PDF", type=["pdf"])
    if uploaded:
        with open(uploaded.name, "wb") as f:
            f.write(uploaded.getbuffer())
        st.success(f"{uploaded.name} uploaded successfully!")

    # List and download all PDFs in the main directory
    st.subheader("Available PDFs")
    pdf_files = [f for f in os.listdir() if f.endswith(".pdf")]

    if not pdf_files:
        st.info("No PDFs available.")
    else:
        for pdf in pdf_files:
            with open(pdf, "rb") as f:
                st.download_button(
                    label=f"Download {pdf}",
                    data=f,
                    file_name=pdf,
                    mime="application/pdf"
                )

# --- Main App Logic ---
if not st.session_state.logged_in:
    login()
else:
    pdf_dashboard()