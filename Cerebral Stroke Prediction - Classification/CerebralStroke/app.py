# Import libraries
import eda, prediction
import streamlit as st

# Add side bar
navigation = st.sidebar.selectbox('Navigation', ['Home', 'Exploratory Data Analysis', 'Patient Stroke Predictor'])

st.sidebar.markdown('# About')

# Introduction
st.sidebar.write('''This tool is designed to explore and predict the occurrence of cerebral strokes. It employs advanced data analysis and machine learning models to offer insights and predictions that can assist medical professionals and researchers in understanding and mitigating the risks associated with cerebral strokes.''')

# Features
st.sidebar.write('''### Key Features:
- **Exploratory Data Analysis**: Analyze the data to uncover patterns and insights related to cerebral strokes.
- **Stroke Occurrence Predictor**: Use predictive models to forecast the likelihood of cerebral strokes in patients.''')

# Target Audience
st.sidebar.write('''### Who can benefit?
- **Medical Professionals**: Enhance understanding and mitigate risks related to cerebral strokes.
- **Researchers**: Analyze and model cerebral stroke datasets for improved predictive accuracy.
- **Data Scientists**: Develop and evaluate machine learning models for cerebral stroke prediction.''')

# Tools
st.sidebar.write('''### Tools Utilized:
- `Python`: For backend operations and model computations.
- `Streamlit`: For creating this interactive web application.
- `Scikit-learn`: For implementing machine learning models.''')

# Define the Home Page
def show_home():
    
    # Create title and introduction
    st.title('Welcome to Cerebral Stroke Prediction Tool')
    st.write('''This tool provides functionalities for Exploratory Data Analysis and Prediction regarding cerebral stroke occurrences. 
    Use the navigation pane on the left to select the module you wish to utilize.''')
    
    # Add image
    st.image('https://img-cdn.medkomtek.com/FNMimFxhdnKJa2CEO74Suco4-dQ=/730x411/smart/filters:quality(100):format(webp)/article/Qu6dyehWPrqOsLB5w-1Hz/original/050687900_1572589916-Stroke-infarct-By-peterschreiber.media-Shutterstock_1423084877.jpg',
             caption='Source: Klik Dokter')
    
    st.markdown('---')
    
    # Dataset
    st.write('#### 📈 Dataset')
    st.markdown('''The dataset is sourced reliably and contains pertinent information on cerebral stroke occurrences. For additional details or to download the dataset, visit
                [Cerebral Stroke Dataset](https://www.kaggle.com/datasets/shashwatwork/cerebral-stroke-predictionimbalaced-dataset/data).''')
    
    # Problem Statement
    st.write('#### ⚠️ Problem Statement')
    st.markdown('''A healthcare center is facing challenges in **predicting strokes in patients**. This leads to delayed interventions and puts patients lives at risk. This problem comes from the complex nature of stroke symptoms and various risk factors, including age, health condition, and lifestyle choices. Not being able to quickly spot who is at
                high risk of a stroke makes it hard to act fast with medical help. As a result, patients might not get the urgent care they need, which could prevent serious consequences like long-term disability or even death. This situation shows the urgent need for better tools that can predict strokes earlier and customize care to each person's needs.''')    
    st.markdown('''To address this challenges, the company wanted to develop a model capable of analyzing patient data to predict the likelihood of a stroke. By creating this algorithm, the healthcare center will be able to thoroughly analyze various aspects of patient data, such as medical history, lifestyle habits, and physiological indicators, to identify key patterns and risk factors linked to strokes.''')
    
    # Objective
    st.write('#### 💡 Objective')
    st.markdown('''This project focuses on creating a **classification model** to predict strokes, selecting the best performer among `KNN`, `SVM`, `Logistic Regression`, `Decision Tree`, `Random Forest`, and `XGBoost`. The key evaluation metric for assessing model performance is `Recall`, which will be used to determine the effectiveness of each model in identifying stroke cases.''')
    
# Create condition to access different pages
if navigation == 'Home':
    show_home()
elif navigation == 'Exploratory Data Analysis':
    eda.run()
elif navigation == 'Patient Stroke Predictor':
    prediction.run()
