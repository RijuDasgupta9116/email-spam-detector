'''
https://www.kaggle.com/nitsin/notebook82c26e6892

'''

import pickle
import streamlit as st

model = pickle.load(open('Models\\model.pkl','rb'))
vector = pickle.load(open('Models\\vectors.pkl','rb'))

st.title('Email Spam Classifier')

email = st.text_area(label='Enter Email Here')

if st.button('Predict'):
    result = model.predict(vector.transform([email]).toarray())[0]
    if result ==1:
        st.header('This email is spam')
    else:
        st.header('This email is not spam')