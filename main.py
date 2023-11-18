import streamlit as st
from streamlit_webrtc import webrtc_streamer

st.title("Motion Detection")

webrtc_ctx = webrtc_streamer(
    key="object-detection"
)