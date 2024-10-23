import streamlit as st

st.title("Contact Me")
with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    submit_form = st.form_submit_button("Submit")
    if submit_form:
        print("Pressed")