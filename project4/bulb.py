import streamlit as st
import urllib.request as url

cloudapi='http://api.thingspeak.com/update?api_key=7S76TN7V3Y4Q3JFI&field1='

st.title('IoT Bulb Control')
col1,col2=st.columns(2)

if col1.button('Bulb On'):
    st.success('Bulb On')
    url.urlopen(cloudapi+'10')

if col2.button('Bulb Off'):
    st.error('Bulb Off')
    url.urlopen(cloudapi+'0')
