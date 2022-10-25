import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
# import template_matching as tmp
"""
    # WEB CỦA LONG
"""

st.balloons()
st.video("https://www.youtube.com/watch?v=Y_7-4jCVVGM",format="video/mp4", start_time=100)
st.audio("https://open.spotify.com/track/1wtOxkiel43cVs0Yux5Q4h?si=8954b0fa7d554665")
st.markdown("""# File""")
uploaded_file = st.file_uploader("Chọn ảnh")
if uploaded_file is not None:
    # To read file as bytes and write to local disk
    bytes_data = uploaded_file.getvalue()
    # st.write(bytes_data)
    img_path = 'data/'+uploaded_file.name
    with open(img_path,"wb") as f: 
        f.write(bytes_data)
    # Filter ảnh
    kernel1 = np.ones((5, 5), np.float32)/30
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cot1, cot2, cot3 = st.columns(3)
    with cot1:
        st.header("Ảnh gốc nè")
        st.image(img)                
    result = cv2.filter2D(img,-1,kernel1)   
    with cot2:
        st.header("Ảnh tối hơn 1 xíu")
        st.image(result) 
    with cot3:
        st.header("Ảnh dạng grayscale")
        st.image(cv2.cvtColor(result, cv2.COLOR_RGB2GRAY))
    st.markdown("""# Template""")

    uploaded_file1 = st.file_uploader("Chọn template")
    if uploaded_file1 is not None:
        # To read file as bytes and write to local disk
        bytes_data = uploaded_file1.getvalue()
        temp_path = 'data/'+uploaded_file1.name
        with open(temp_path,"wb") as f: 
            f.write(bytes_data)
        template = cv2.imread(temp_path,0)
        st.image(template)
    
threshold = st.number_input("Nhập threshold: ")    
button = st.button("Tìm")
# if button: 
#     res = tmp.template_matching(img,template,threshold)   
#     st.image(res)   
