import streamlit as st

st.set_page_config(layout="wide")

video_html = """
	<style>
		#myVideoContainer {
			height: 100vh;
			width: 25%;
			float: right;
			position: fixed;
			top: 0;
			right: 0;
			overflow: hidden;
			border: 2px solid black;
		}

		#myVideo {
			position: absolute;
			top: 0;
			left: 0;
			width: 100%;
			height: 100%;
		}
	</style>
	<div id="myVideoContainer">
		<video autoplay muted loop id="myVideo">
			<source src="https://video.twimg.com/ext_tw_video/1626920076204032000/pu/vid/540x720/3chX4Ud9SsEnLf5m.mp4?tag=12">
			Your browser does not support HTML5 video.
		</video>
	</div>
"""

col1, col2 = st.beta_columns([1, 3])
with col1:
    st.title('My App Title')
    st.write('This is some text on the left column.')

with col2:
    st.markdown(video_html, unsafe_allow_html=True)
