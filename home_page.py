import streamlit as st


# Set the page title and favicon
st.set_page_config(page_title="Waves of The Heart", page_icon=":heartbeat:")

st.markdown(
        f"""
        <div style='text-align: center;'>
            <h1 style='font-family: Yasashii Bold; color: red;'>Waves of The Heart</h1>
            <p>Automated Heart Sound Classification Tool</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


st.image("/home/mer/Pictures/Screenshots/Screenshot from 2023-02-24 16-21-01.png", use_column_width=True, output_format="PNG")

audio = st.file_uploader('Upload audio file', type=['wav'])

if audio is not None:
    st.write('Classifying...')
