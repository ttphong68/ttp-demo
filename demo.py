#----------------------------------------------------------------------------------------------------
#### HV : THÁI THANH PHONG
#### SN : 14/03/1968
#### ĐỒ ÁN TỐT NGHIỆP : Project 1 Data Prepreocessing
#### MÔN HỌC : Data science
#----------------------------------------------------------------------------------------------------
import streamlit as st
st.set_page_config(page_title="Recommendation app", page_icon="https://www.analyticsvidhya.com/wp-content/uploads/2016/03/ri1.png")
st.title('RECOMMENNDATION SYSTEM APP')

menu = ['Overview', 'Build Model', 'New Prediction']
choice = st.sidebar.selectbox('Menu', menu)

if choice == 'Overview':
    st.subheader('Overview')

    st.write('''
    This project is about sentiment analysis of Vietnamese comments on Shopee. 
    The dataset is collected from Shopee website. 
    The dataset contains 2 columns: rating and comment. 
    The rating is from 1 to 5. 
    The comment is the comment of customers after they buy products on Shopee. 
    The goal of this project is to build a model to predict the sentiment of comments. 
    The sentiment is positive or negative. 
    ''')
    st.write('''
    The dataset has 2 classes: positive and negative. 
    ''')
    st.write('''
    The model is built with Logistic Regression and applying oversampling data:
    - The model has 86% accuracy.
    - The model has 94% precision for the positive class.
    - The model has 85% recall for the positive class.
    - The model has 73% precision for the negative class.
    - The model has 88% recall for the negative class. 
    ''')
elif choice == 'Build Model':
    st.subheader('Build Model')
    st.write('#### Data Preprocessing')
    st.write('##### Show data')

elif choice == 'New Prediction':
    st.subheader('New Prediction')
    st.write('''
    Input a comment and the model will predict the sentiment of the comment. 
    ''')
