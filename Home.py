import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/me.jpeg")

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

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=',')

with col3:
    for idx, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for idx, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")