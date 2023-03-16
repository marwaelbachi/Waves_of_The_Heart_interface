import streamlit as st

st.set_page_config(layout="wide")

video_html = """
	<style>
		#myVideo {
			position: fixed;
			top: 0;
			left: 0;
			width: 100vw;
			height: 100vh;
		}
	</style>
	<video autoplay muted loop id="myVideo">
		<source src="https://video.twimg.com/ext_tw_video/1626920076204032000/pu/vid/540x720/3chX4Ud9SsEnLf5m.mp4?tag=12">
		Your browser does not support HTML5 video.
	</video>
"""

st.markdown(video_html, unsafe_allow_html=True)
st.title('Video page')
