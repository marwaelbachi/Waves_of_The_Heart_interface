import streamlit as st

st.set_page_config(layout="wide")

image_html = """
    <style>
        #myImageContainer {
            width: 100%;
            height: auto;
            border: 2px solid black;
            overflow: hidden;
        }

        #myImage {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
    </style>
    <div id="myImageContainer">
        <img src="{}" alt="My Image" id="myImage">
    </div>
"""

col1, col2 = st.columns([1, 3])
with col1:
    st.title('My App Title')
    st.write('This is some text on the left column.')

with col2:
    image_path = "/home/mer/code/Le wagon project/Screenshot from 2023-02-24 11-54-12.png"
    st.markdown(image_html.format(image_path), unsafe_allow_html=True)
