# Import libraries
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create program
def run():
    
    # Load data
    data = pd.read_csv('dataset.csv')

    # Main page setup
    st.title('Credit Card Users Data Exploration')

    # User selection
    st.header('User Input Features')
    
    # Age slider
    selected_age = st.slider('Filter by age',
                             min_value=int(data['age'].min()),
                             max_value=int(data['age'].max()),
                             value=(int(data['age'].min()), int(data['age'].max())))
    
    # Sex selection
    sex_mapping = {'Male': 1, 'Female': 2}
    sex_options = ['Male', 'Female']
    sex_selection = st.multiselect('Filter by gender', options=sex_options, default=sex_options)
    
    # Convert selected sex from names to numerical values for filtering
    selected_sex_numerical = []
    for sex in sex_selection:
        selected_sex_numerical.append(sex_mapping[sex])

    # Filtering data based on user selection
    filtered_data = data[(data['age'] >= selected_age[0]) & (data['age'] <= selected_age[1]) & (data['sex'].isin(selected_sex_numerical))]
    st.write('Data Dimension: ' + str(filtered_data.shape[0]) + ' rows and ' + str(filtered_data.shape[1]) + ' columns.')
    st.dataframe(filtered_data)

    # Visualization selections
    st.header('Visualization Settings')
    plot_type = st.selectbox('Select the type of plot', ['Scatter Plot', 'Bar Chart', 'Histogram'])

    # Create condition for selected visualization
    
    # Histogram
    if plot_type == 'Histogram':
        st.subheader('Histogram')
        column = st.selectbox('Select column to display', options=['age', 'limit_balance'])
        fig, ax = plt.subplots()
        sns.histplot(data=filtered_data, x=column, kde=True, ax=ax, color='skyblue')
        ax.set_title(f'{column} Distribution')
        st.pyplot(fig)

    # Bar Chart
    elif plot_type == 'Bar Chart':
        st.subheader('Bar Chart')
        column = st.selectbox('Select column to display', options=['sex', 'education_level', 'marital_status'])
        fig, ax = plt.subplots()
        sns.countplot(data=filtered_data, x=column, ax=ax, palette='coolwarm')
        ax.set_title(f'Count of {column}')
        st.pyplot(fig)

    # Scatter Plot
    elif plot_type == 'Scatter Plot':
        st.subheader('Scatter Plot')
        x_axis = st.selectbox('X-axis', options=['age', 'limit_balance'])
        y_axis = st.selectbox('Y-axis', options=['bill_amt_1', 'bill_amt_2', 'bill_amt_3', 'bill_amt_4', 'bill_amt_5', 'bill_amt_6',
                                                 'pay_amt_1', 'pay_amt_2', 'pay_amt_3', 'pay_amt_4', 'pay_amt_5', 'pay_amt_6'])
        fig, ax = plt.subplots()
        sns.scatterplot(data=filtered_data, x=x_axis, y=y_axis, ax=ax, hue='sex', palette='coolwarm')
        ax.set_title(f'{x_axis} vs {y_axis}')
        st.pyplot(fig)
