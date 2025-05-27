import streamlit as st

# --- Hardcoded credentials ---
USERNAME = "user"
PASSWORD = "pass123"

# --- Session state ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = {}

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

# --- PDF Upload & Download Page ---
def pdf_dashboard():
    st.title("PDF Dashboard")

    uploaded = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)
    if uploaded:
        for file in uploaded:
            st.session_state.uploaded_files[file.name] = file

    if not st.session_state.uploaded_files:
        st.info("No PDFs uploaded yet.")
    else:
        st.subheader("Available PDFs")
        for name, file in st.session_state.uploaded_files.items():
            st.download_button(
                label=f"Download {name}",
                data=file.getvalue(),
                file_name=name,
                mime="application/pdf"
            )

# --- Main App Logic ---
if not st.session_state.logged_in:
    login()
else:
    pdf_dashboard()