import boto3
import streamlit as st
from PIL import Image
import os

k=os.listdir('faces') # list of faces

st.title('Face Recognition System') # place the title of web app

img_file=st.file_uploader('Upload your face image',type=['png','jpg','jpeg']) # uploading the image

if img_file is not None:
    file_details={} # get img file details
    file_details['name']=img_file.name
    file_details['size']=img_file.size
    file_details['type']=img_file.type
    st.write(file_details)

    with open('src.jpg','wb') as f: # save img file
        f.write(img_file.getbuffer())
    
    st.image(Image.open(img_file),width=250) # display the file which I've uploaded

    client=boto3.client('rekognition')
    for i in k:
        sourceImage=open('src.jpg','rb')
        targetImage=open('faces/'+i,'rb')
        response=client.compare_faces(SimilarityThreshold=70,SourceImage={'Bytes': sourceImage.read()},TargetImage={'Bytes':targetImage.read()})
        # st.write(response['FaceMatches'])
        if(len(response['FaceMatches'])>0):
            i=i.split('.')[0]
            st.success('Face Matched with '+i)
            break



    

    
