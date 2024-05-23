# Import libraries
import streamlit as st
import pandas as pd
import pickle
from time import sleep

# Load the best model
with open('best_rf_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Create function to make the app
def run():
    
    # Add title
    st.title('Patient Stroke Predictor')

    # Create form
    with st.form('Predict Stroke'):
        
        with st.expander("Personal Information"):
            col1, col2, col3 = st.columns(3)

            # Patient ID
            with col1:
                id = st.number_input("Patient ID", help="Enter patients' ID. Example: 1234", step=1)

            # Gender
            with col2:
                gender = st.selectbox('Gender', ['Male', 'Female', 'Others'], help="Select the patient's gender.")

            # Age
            with col3:
                age = st.number_input('Age', min_value=1, max_value=100, help="Enter the patient's age (between 1 and 100).")

            # Marital status
            ever_married = st.selectbox('Ever Married', ['Yes', 'No'], help="Select if the patient is ever married or not.")

            # Type of work
            work_type = st.selectbox('Type of Work', ['Government Employee', 'Private-sector Employee', 'Self-Employed', 'Not in Labor Force (Child)', 'Never work'], help="Select the patient's type of work.")
            work_type_map = {'Government Employee': 'Govt_job',
                            'Private-sector Employee': 'Private',
                            'Self-Employed': 'Self-employed',
                            'Not in Labor Force (Child)': 'Children',
                            'Never work': 'Never_worked'}
            work_type = work_type_map[work_type]

            # Type of residence
            residence_type = st.selectbox('Type of Residence', ['Rural', 'Urban'], help="Select the type of residence.")

        with st.expander("Health Information"):

            # Disease
            disease_options = ['Hypertension', 'Heart Disease']
            selected_diseases = st.multiselect('Disease', disease_options, help="Select any diseases the patient has. If None, leave it empty.")

            # Average glucose levels
            avg_glucose_level = st.text_input('Average glucose level (in mg/dL)', value='0', help="Enter the patient's average glucose level in mg/dL. Must be between 0 and 2000.")

            # BMI
            bmi = st.text_input('Body Mass Index (BMI)', value='10', help="Enter the patient's Body Mass Index (BMI). Must be between 10 and 150.")

        with st.expander('Lifestyle Factor'):
            
            # Smoking status
            smoking_status = st.radio('Smoking status', ['Smokes', 'Formerly smokes', 'Never smoked'], help="Select the patient's smoking status.")

        submit = st.form_submit_button("Predict Stroke Status")

        # Error handling
        error = False
        try:
            avg_glucose_level = float(avg_glucose_level)
            if not (0 <= avg_glucose_level <= 2000):
                st.error('Please enter a valid glucose level between 0 and 2000 mg/dL.')
                error = True
        except ValueError:
            st.error('Please enter a valid numerical value for the glucose level.')
            error = True

        try:
            bmi = float(bmi)
            if not (10 <= bmi <= 150):
                st.error('Please enter a valid BMI score between 10 and 150.')
                error = True
        except ValueError:
            st.error('Please enter a valid numerical value for the BMI score.')
            error = True

    if submit and not error:
        data_inf = pd.DataFrame([{
            'id': id,
            'gender': gender,
            'age': age,
            'hypertension': 1 if 'Hypertension' in selected_diseases else 0,
            'heart_disease': 1 if 'Heart Disease' in selected_diseases else 0,
            'ever_married': ever_married,
            'work_type': work_type,
            'Residence_type': residence_type,
            'avg_glucose_level': avg_glucose_level,
            'bmi': bmi,
            'smoking_status': smoking_status}])

        # Add progression
        bar = st.progress(0)
        for percent_complete in range(101):
            sleep(0.005)
            bar.progress(percent_complete)
        
        # Prediction result
        prediction = model.predict(data_inf)[0]
        
        # Probability of stroke
        prediction_prob = model.predict_proba(data_inf)[0][1]
        probability_percentage = prediction_prob * 100
        bar.progress(100)
        st.success('Prediction Completed!')

        # Show prediction results
        if prediction == 0:
            st.write(f'The patient is not experiencing a stroke, with the stroke probability being {probability_percentage:.2f}%.')
        elif prediction == 1:
            st.write(f'The patient has experienced a stroke, with a {probability_percentage:.2f}% probability.')

if __name__ == '__main__':
    run()
