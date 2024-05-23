# Import libraries
import streamlit as st
import pandas as pd
import pickle

# Load the best model
with open('best_svm_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Create function to make the app
def run():
    
    # Add title
    st.title('Credit Card Default Payment Predictor')
    
    # Create form
    with st.form('Predict Default Status'):
        st.subheader('Personal Information')
        
        col1, col2, col3 = st.columns(3)
        
        # Limit balance
        with col1:
            limit_balance = st.number_input('Limit Balance (NTD)*', help="Enter the credit limit amount. This is the maximum amount the client is allowed to borrow.")
        
        # Sex
        with col2:
            sex = st.selectbox('Gender', ['Male', 'Female'], help="Select the client's gender. This is used for demographic analysis.")
            if sex == 'Male':
                sex = 1
            elif sex == 'Female':
                sex = 2
        
        # Age
        with col3:
            age = st.number_input('Age', min_value=18, max_value=100, help="Enter the client's age. Clients must be at least 18 years old.")
        
        # Educational level
        educational_level = st.selectbox('Educational Level', ['Graduate School', 'University', 'High School', 'Others'],
                                         help="Select the client's highest completed educational level.")
        education_map = {'Graduate School': 1, 'University': 2, 'High School': 3, 'Others': 4}
        educational_level = education_map[educational_level]
        
        # Marital status
        marital_status = st.selectbox('Marital Status', ['Single', 'Married', 'Others'],
                                      help="Select the client's marital status. This information is used for demographic analysis.")
        marital_map = {'Single': 1, 'Married': 2, 'Others': 3}
        marital_status = marital_map[marital_status]
        
        st.subheader('Financial Information')
        
        # Repayment status
        expander_repayment = st.expander("Repayment Status")
        with expander_repayment:
            pay_6 = st.slider('April', min_value=0, max_value=20, value=0, help="Repayment status for each month. '0' means no delayed payment, '1' means delayed 1 month, etc.")
            pay_5 = st.slider('May', min_value=0, max_value=20, value=0)
            pay_4 = st.slider('June', min_value=0, max_value=20, value=0)
            pay_3 = st.slider('July', min_value=0, max_value=20, value=0)
            pay_2 = st.slider('August', min_value=0, max_value=20, value=0)
            pay_0 = st.slider('September', min_value=0, max_value=20, value=0)
        
        # Bill amounts
        expander_bill = st.expander("Monthly Bill Amounts")
        with expander_bill:
            bill_amt_6 = st.number_input('Bill Amount in April*', help="Enter the bill amount for April.")
            bill_amt_5 = st.number_input('Bill Amount in May*', help="Enter the bill amount for May.")
            bill_amt_4 = st.number_input('Bill Amount in June*', help="Enter the bill amount for June.")
            bill_amt_3 = st.number_input('Bill Amount in July*', help="Enter the bill amount for July.")
            bill_amt_2 = st.number_input('Bill Amount in August*', help="Enter the bill amount for August.")
            bill_amt_1 = st.number_input('Bill Amount in September*', help="Enter the bill amount for September.")
        
        # Previous payment amounts
        expander_payment = st.expander("Previous Payment Amounts")
        with expander_payment:
            pay_amt_1 = st.number_input('Previous Payment in April*', help="Enter the payment amount made in April.")
            pay_amt_2 = st.number_input('Previous Payment in May*', help="Enter the payment amount made in May.")
            pay_amt_3 = st.number_input('Previous Payment in June*', help="Enter the payment amount made in June.")
            pay_amt_4 = st.number_input('Previous Payment in July*', help="Enter the payment amount made in July.")
            pay_amt_5 = st.number_input('Previous Payment in August*', help="Enter the payment amount made in August.")
            pay_amt_6 = st.number_input('Previous Payment in September*', help="Enter the payment amount made in September.")
    
        submit = st.form_submit_button("Predict Default Status")
        
        required_questions = [limit_balance, bill_amt_6, bill_amt_5, bill_amt_4, bill_amt_3,
                              bill_amt_2, bill_amt_1, pay_amt_6, pay_amt_5, pay_amt_4, pay_amt_3, pay_amt_2, pay_amt_1]

    
    if submit:
        if all(required_questions):
            data_inf = pd.DataFrame([{
                'limit_balance': limit_balance,
                'sex': sex,
                'education_level': educational_level,
                'marital_status': marital_status,
                'age': age,
                'pay_0': pay_0,
                'pay_2': pay_2,
                'pay_3': pay_3,
                'pay_4': pay_4,
                'pay_5': pay_5,
                'pay_6': pay_6,
                'bill_amt_1': bill_amt_1,
                'bill_amt_2': bill_amt_2,
                'bill_amt_3': bill_amt_3,
                'bill_amt_4': bill_amt_4,
                'bill_amt_5': bill_amt_5,
                'bill_amt_6': bill_amt_6,
                'pay_amt_1': pay_amt_1,
                'pay_amt_2': pay_amt_2,
                'pay_amt_3': pay_amt_3,
                'pay_amt_4': pay_amt_4,
                'pay_amt_5': pay_amt_5,
                'pay_amt_6': pay_amt_6}])
        
            # Predict default status
            prediction = model.predict(data_inf)[0]
            
            # Show prediction results
            if prediction == 0:
                st.success('Prediction Completed: Non-Default')
            elif prediction == 1:
                st.error('Prediction Completed: Default')
        else:
            st.warning('Please fill in all required fields.')

if __name__ == '__main__':
    run()
