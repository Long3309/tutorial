import streamlit as st
import cv2
img_file_buffer = st.camera_input("Take a picture")
if img_file_buffer:
    bytes_data = img_file_buffer.getvalue()
        # st.write(bytes_data)
    img_path = 'data/'+img_file_buffer.name
    with open(img_path,"wb") as f: 
        f.write(bytes_data)
    st.image(img_file_buffer)
    
