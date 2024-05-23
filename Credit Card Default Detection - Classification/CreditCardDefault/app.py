# Import libraries
import eda, prediction
import streamlit as st

# Add side bar
navigation = st.sidebar.selectbox('Navigation', ['Home', 'Exploratory Data Analysis', 'Default Payment Predictor'])

st.sidebar.markdown('# About')

# Introduction
st.sidebar.write(''' This application used as a comprehensive tool for exploring and predicting credit card defaults. It utilizes advanced data analysis and machine learning models to provide insights and predictions that can help financial analysts and 
decision-makers understand credit risks more effectively.''')

# Features
st.sidebar.write('''### Features:
- **Exploratory Data Analysis**: Dive deep into the data to uncover patterns and insights related to credit card defaults.
- **Default Payment Predictor**: Use predictive models to forecast the probablity of credit card defaults in the upcoming period.''')

# Target Market
st.sidebar.write('''### Who is this for?
- **Financial Analysts**: To assist in understanding and mitigating risks associated with credit defaults.
- **Credit Risk Managers**: To evaluate and manage risks, improving financial decisions.
- **Data Scientists**: To explore and model credit risk datasets for better predictive accuracy.''')

# Tools
st.sidebar.write('''### Tools Used:
- `Python`: For backend operations and model computations.
- `Streamlit`: For creating this interactive web application.
- `Scikit-learn`: For implementing machine learning models.''')

# Define the Home Page
def show_home():
    
    # Create title and introduction
    st.title('Welcome to Credit Analysis Tool')
    st.write('''This application provides tools for both Exploratory Data Analysis and Prediction on credit card default payments. 
    Use the navigation pane on the left to select the module you would like to use.''')
    
    # Add image
    st.image('https://img.pikbest.com/wp/202346/credit-card-icon-aesthetic-3d-design-of-cards_9748274.jpg!bw700',
             caption='Resource: Pik Best')
    
    st.markdown('---')
    
    # Dataset
    st.write('#### 📊 Dataset')
    st.markdown(''' The dataset is obtain from Big Query about Credit Card Default. For further details or to download the dataset, please visit
                [Big Query Credit Card Default Dataset](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=ml_datasets&t=credit_card_default&page=table&project=hacktiv8-sql-417802&ws=!1m9!1m3!3m2!1sbigquery-public-data!2sml_datasets!1m4!4m3!1sbigquery-public-data!2sml_datasets!3scredit_card_default).''')
    
    # Problem Statement
    st.write('#### ❗Problem Statement')
    st.markdown('''The company struggles to assess credit risks accurately, requiring an advanced model to **predict default probabilities** in upcoming periods. Default occurs when borrowers fail to meet credit card payments, leading to financial losses,
             increased costs for recovery efforts, and can hurt company's reputation. To address these challenges, the company needs an advanced predictive model that can forecast default probabilities for borrowers in the upcoming periods. 
             By accurately predicting default risks, the company can take proactive measures to minimize losses, manage risks effectively, and improve overall financial stability and performance.''')
    
    # Objective
    st.write('#### 🎯 Objective')
    st.markdown('''This project aims to to develop a classification model using `K-Nearest Neighbors (KNN)`, `Support Vector Machine (SVM)`, and `Logistic Regression` algorithms to forecast credit card defaults for the next month. The evaluation metric employed
             for model performance assessment is the `Recall` to calculate each model's performance.''')
    
# Create condition to access different pages
if navigation == 'Home':
    show_home()
elif navigation == 'Exploratory Data Analysis':
    eda.run()
elif navigation == 'Default Payment Predictor':
    prediction.run()
