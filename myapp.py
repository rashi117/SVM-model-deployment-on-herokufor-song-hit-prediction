#!/usr/bin/env python
# coding: utf-8

# In[30]:


import streamlit as st
import pickle
import numpy as np


# In[31]:


model= pickle.load(open('mymodel.pkl','rb'))


# In[32]:


def predict(danceability, energy,key,mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,duration_ms,loudness):
    input= np.array([[danceability, energy,key,mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,duration_ms,loudness]]).astype(np.float)
    prediction = model.predict(input)

    if prediction[0] == 0:
            pred ="song is flop"
    else:
            pred ="song is hit"
    return pred


# In[33]:


def main():
    st.title("Song Hit or Not Prediction App")
   
    danceability = st.text_input("danceability")
    energy = st.text_input("energy")
    key = st.text_input("key")
    mode = st.text_input("mode")
    speechiness = st.text_input("speechiness")
    acousticness = st.text_input("acousticness")
    instrumentalness = st.text_input("instrumentalness")
    liveness = st.text_input("liveness")
    valence = st.text_input("valence")
    tempo = st.text_input("tempo")
    duration_ms = st.text_input("duration_ms")
    loudness= st.text_input("loudness")
    
   
    if st.button("Predict"):
        output=predict(danceability, energy,key,mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,duration_ms,loudness)
        st.success("{} ".format(output))
        
        
if __name__=="__main__":
    main()
    
    
    
    

