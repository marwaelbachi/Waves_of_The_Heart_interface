import streamlit as st


# Set the page title and favicon
st.set_page_config(page_title="Waves of The Heart", page_icon=":heartbeat:")

# Define the main header and subheader
st.markdown(
    f"""
    <div style='text-align: center;'>
        <h1 style='font-family: Yasashii Bold; color: red;'>Waves of The Heart</h1>
        <p>Automated Heart Sound Classification Tool</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Define the HTML for the image container
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
            border-left: 2px solid black;
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
"""

# Display the image
image_path = "/home/mer/code/Le wagon project/Screenshot from 2023-02-24 11-54-12.png"
st.markdown(image_html, unsafe_allow_html=True)
st.image(image_path, use_column_width=False)

# Add your content in the main section of the page
st.write("This is where your content will go.")
