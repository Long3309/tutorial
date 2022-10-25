import streamlit as st 
import cv2
st.set_page_config(
    page_title ="Multipage Apps",
    page_icon= "😊"
)
"""# Main Page"""
st.header("Radio")
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
    st.session_state.horizontal = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable radio widget", key="disabled")
    st.checkbox("Orient radio options horizontally", key="horizontal")

with col2:
    st.radio(
        "Set label visibility 👇",
        ["visible", "hidden", "collapsed"],
        key="visibility",
        disabled=st.session_state.disabled,
        horizontal=st.session_state.horizontal,
        # label_visibility=st.session_state.visibility
    )
color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)

