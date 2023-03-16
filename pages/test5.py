import streamlit as st

st.set_page_config(layout="wide")

image_html = """
    <style>
        #myImageContainer {
            height: 100vh;
            width: 25%;
            float: right;
            position: fixed;
            top: 0;
            right: 0;
            overflow: hidden;
            #border: 2px solid black;
        }

        #myImage {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
    </style>
    <div id="myImageContainer">
        <img src="{}" alt="My Image" id="myImage">
    </div>
"""

col1, col2, col3, col4 = st.columns([1, 2, 3, 4])
with col1:
    st.title('My App Title')
    st.write('This is some text on the left column.')

with col4:
    image_path = "/home/mer/code/Le wagon project/Screenshot from 2023-02-24 11-54-12.png"
    st.markdown(image_html, unsafe_allow_html=True)
    st.image(image_path, use_column_width=False)
    #st.markdown(image_html, unsafe_allow_html=True)
    #image_path =
  # replace this with the actual path of your image
    #st.image(image_path, use_column_width=False, width=300)
