import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/me.jpeg", width=600)

with col2:
    st.title("Thiemo Morth")
    content = """
    Hi, I am Thiemo! I am a Software Architect, Java and Python programmer, a family father and a Mountainbike 
    rider. I graduated in 2008 with a Master of Science in Computer Sciences from the University of Applied Science 
    Trier in Germany. ...
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)