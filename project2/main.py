import streamlit as st
import boto3
from PIL import Image

st.title('Celebrity Recognition System')
imgfile=st.file_uploader('upload an image',type=['png','jpg','jpeg'])

if imgfile is not None:
    st.image(Image.open(imgfile))
    with open('src.jpg','wb') as f:
        f.write(imgfile.getbuffer())
    imageSource=open('src.jpg','rb')
    client=boto3.client('rekognition')
    response=client.recognize_celebrities(
        Image={'Bytes':imageSource.read()}
    )
    #st.write(response)
    if response['CelebrityFaces']:
        st.success(response['CelebrityFaces'][0]['Name'])
        st.write(response['CelebrityFaces'][0]['Urls'])
