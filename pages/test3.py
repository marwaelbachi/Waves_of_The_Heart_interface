import streamlit as st
import base64


# Define image location
image_location = "/home/mer/code/Le wagon project/Screenshot from 2023-02-24 11-54-12.png"

# Add border to image container and set its width and height to 25% and 100% respectively
st.markdown(
    f'<div style="float: right; border: 2px solid black; padding: 10px; width: 25%; height: 100%;"><img src="data:image/png;base64,{base64.b64encode(open(image_location, "rb").read()).decode()}" alt="My Image" style="height: 100%; width: 100%;"></div>',
    unsafe_allow_html=True,
)

# Add header and subheader
st.title("My Page Header")
st.subheader("My Page Subheader")

# Add remaining content here
