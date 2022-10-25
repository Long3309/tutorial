from tkinter.tix import IMAGE
from turtle import color
from PIL import Image
import streamlit as st
import cv2
import numpy as np


st.markdown("""
           # Đây là bài tutorial
           ## 1.1 Heading 1
           ### 1.2 Heading 2    
           """)

a_value = st.number_input("Nhap a: ")
b_value = st.number_input("Nhap b: ")
# option = st.selectbox(
#     'How would you like to be contacted?',
#     ('Cộng', 'Trừ', 'Nhân','Chia'))
# st.write('You selected:', option)
option = st.radio(
    'Chọn phép tính?',
    ('Cộng', 'Trừ', 'Nhân','Chia'))

button = st.button("Tính")
# Button event
if button:
    if option == 'Cộng':
        st.text_input("Kết quả",float(a_value) + float(b_value))
    if option == 'Trừ':
        st.text_input("Kết quả",float(a_value) - float(b_value))
    if option == 'Nhân':
        st.text_input("Kết quả",float(a_value) * float(b_value))
    if option == 'Chia':
        st.text_input("Kết quả",float(a_value) / float(b_value))
else:
    st.text("Kết quả")
# End Button event

col1, col2, col3 = st.columns(3)
with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")
with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")
with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

st.markdown("""# Tab""")
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
   
st.markdown("""# File""")
uploaded_file = st.file_uploader("Chọn ảnh")
if uploaded_file is not None:
    # To read file as bytes and write to local disk
    bytes_data = uploaded_file.getvalue()
    # st.write(bytes_data)
    img_path = 'data/'+uploaded_file.name
    with open(img_path,"wb") as f: 
        f.write(bytes_data)
    #Filter ảnh
    kernel1 = np.ones((5, 5), np.float32)/30
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cot1, cot2, cot3 = st.columns(3)
    with cot1:
        st.header("Ảnh gốc")
        st.image(img)                
    result = cv2.filter2D(img,-1,kernel1)   
    with cot2:
        st.header("Ảnh tối hơn 1 xíu")
        st.image(result) 
    with cot3:
        st.header("Ảnh dạng grayscale")
        st.image(cv2.cvtColor(result, cv2.COLOR_RGB2GRAY))