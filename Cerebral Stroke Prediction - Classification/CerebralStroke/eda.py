# Import libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Define custom color palette
custom_palette = px.colors.qualitative.Set3

# Create the main program
def run():
    
    # Load the dataset
    data = pd.read_csv('dataset.csv')
    
    # Add title to the app
    st.title('Exploratory Data Analysis')
    
    # Checkbox to display raw data
    if st.checkbox('Show raw data'):
        st.markdown('#### Raw Data')
        st.write(data)
    
    # Dropdown for different analysis options
    option = st.selectbox('Select Analysis', ('Overview', 'Distribution Plots', 'Categorical Analysis', 'Correlation Heatmap', 'Stroke Risk Analysis'))
    
    # Overview analysis
    if option == 'Overview':
        st.subheader('Dataset Overview')
        st.write('This dataset contains a diverse range of personal information about patients, along with details regarding their stroke condition. Its purpose is to discover correlations between different variables and the occurrence of strokes.')
        st.markdown('###### Summary Statistics')
        numerical_columns = data[['age', 'avg_glucose_level', 'bmi', 'stroke']]
        st.write(numerical_columns.describe())
        st.write('The dataset covers a broad age range, from infants to 82 years old, with an average BMI of 27.7, classifying the average person as overweight. The average glucose level is slightly elevated, which might suggest a risk of diabetes. Stroke events are rare, affecting only about 1.8% of the population.')
    
    # Distribution plots analysis
    elif option == 'Distribution Plots':
        st.subheader('Distribution of Numerical Variables')
        numerical_columns = st.multiselect('Select columns to visualize', ['age', 'avg_glucose_level', 'bmi'], ['age', 'avg_glucose_level', 'bmi'])
        
        # Add insight for each variable
        column_descriptions = {
            'age': "The age distribution in the dataset covers a wide range, including individuals from young to elderly ages. Two noticeable peaks emerge: one in the late 20s and a smaller one around the late 50s. However, there's a decrease in the number of individuals in older age brackets, particularly beyond 60 years old, indicating a trend of fewer entries in these age ranges.",
            'avg_glucose_level': "The average glucose levels follow a roughly normal distribution, peaking around 100 mg/dL, a typical value for a healthy adult population. However, there's a tail extending to higher glucose levels, indicating a subset of individuals with elevated levels, possibly suggestive of diabetes or pre-diabetic conditions.",
            'bmi': 'The BMI distribution shows a slight right skew, indicating more individuals with a BMI above the mean than below it. The peak is around 28, categorized as overweight, suggesting a considerable portion of the population falls into the overweight or obese category.'}
        
        for idx, col in enumerate(numerical_columns):
            fig = px.histogram(data, x=col, title=f'Distribution of {col.title().replace("_", " ")}', nbins=30, color_discrete_sequence=[custom_palette[idx]])
            st.plotly_chart(fig)
            st.markdown(column_descriptions[col])
    
    # Categorical analysis
    elif option == 'Categorical Analysis':
        st.subheader('Categorical Data Analysis')
        categorical_columns = st.multiselect('Select columns to visualize', ['gender', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type', 'smoking_status'], ['gender', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type', 'smoking_status'])
        
        # Add insight for each variable
        column_descriptions = {
            'gender': "The dataset predominantly includes females, comprising around 28,000 individuals. Interestingly, there are no entries categorized as 'Other,' indicating a binary gender representation.",
            'hypertension': 'A significant majority, nearly 40,000 individuals, do not have hypertension, while a smaller fraction, approximately 5,000 individuals, have been diagnosed with this condition.',
            'heart_disease': 'Similar to hypertension, the dataset shows a significant majority without heart disease, totaling almost 40,000 individuals. In contrast, those with heart disease are notably fewer, around 2,000 individuals.',
            'ever_married': 'The dataset is mostly composed of individuals who have been or are currently married, accounting for approximately 30,000 individuals. The unmarried group is considerably smaller, comprising around 10,000 individuals.',
            'work_type': 'The largest segment of the dataset is individuals employed in private jobs, numbering about 25,000. Self-employed individuals and children form the next largest categories, with approximately 8,000 and 5,000 individuals, respectively, followed by smaller numbers in Govt_job and almost negligible numbers in Never_worked.',
            'Residence_type': 'The distribution between urban and rural residents is nearly balanced, with slightly more urban residents at about 21,756 compared to 21,644 in rural areas.',
            'smoking_status': 'A significant portion of the dataset, approximately 16,000 individuals, have never smoked. Former smokers make up around 7,000 individuals, while current smokers number around 6,500.'}
        
        for idx, col in enumerate(categorical_columns):
            fig = px.histogram(data, col, title=f'{col.title().replace("_", " ")} Distribution', color_discrete_sequence=[custom_palette[idx]])
            st.plotly_chart(fig)
            st.markdown(column_descriptions[col])
    
    # Correlation heatmap analysis
    elif option == 'Correlation Heatmap':
        numerical_columns = data[['age', 'avg_glucose_level', 'bmi', 'stroke']]
        corr = numerical_columns.corr()
        fig = px.imshow(corr, color_continuous_scale='viridis', title='Correlation Heatmap')
        st.plotly_chart(fig)
        st.markdown('The correlation heatmap shows a notable moderate correlation between age and BMI, indicating that as individuals age, their BMI tends to increase. This pattern highlights the importance of monitoring and managing BMI as part of aging health strategies. Additionally, the heatmap does not show strong direct correlations between these factors and stroke occurrence, suggesting that stroke risk may be influenced by a combination of factors rather than a single measure. This calls for a multifactorial approach in stroke prevention efforts.')
    
        
    # Stroke risk analysis
    elif option == 'Stroke Risk Analysis':
        st.subheader('Analysis of Stroke Risk by Various Factors')
        categorical_columns = st.multiselect('Select columns to visualize', ['gender', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type'], ['gender', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type'])
        
        # Add insight for each variable
        column_descriptions = {
            'gender': 'The bar chart shows more females than males in the dataset, with similar stroke rates across genders. However, the "Other" category is 0.. This suggests that gender may not significantly influence stroke risk in this population.',
            'hypertension': 'The bar chart indicates that individuals without hypertension significantly outnumber those with hypertension in the dataset. However, despite the lower numbers, individuals with hypertension show a noticeable incidence of stroke, suggesting a strong link between hypertension and stroke risk.',
            'heart_disease': 'The chart shows that the majority of the dataset does not have heart disease, but those with heart disease have a higher incidence of stroke. This suggests a significant link between heart disease and increased stroke risk, highlighting heart disease as a critical factor in stroke prevention strategies.',
            'ever_married': "The chart shows more individuals who have been married than those who haven't. Without stroke rates shown, it's unclear if marital status significantly impacts stroke risk. Further analysis is needed to explore this potential relationship.",
            'work_type': "The chart shows that most people in the dataset work in private jobs, followed by self-employed and government jobs. Children and those who've never worked have the lowest counts. Without stroke occurrence rates, it's unclear if work type significantly impacts stroke risk, highlighting the need for further analysis.",
            'Residence_type': "The chart shows an equal number of individuals from rural and urban areas. Without stroke rates, it's unclear if residence type affects stroke risk, indicating a need for deeper analysis."}
        
        for idx, col in enumerate(categorical_columns):
            grouped_data = data.groupby([col, 'stroke']).size().reset_index(name='count')
            fig = px.bar(grouped_data, x=col, y='count', color='stroke', title=f'Stroke Occurrence by {col.title().replace("_", " ")}', color_discrete_sequence=[custom_palette[0], custom_palette[1]], barmode='group')
            st.plotly_chart(fig)
            st.markdown(column_descriptions[col])

# Run the app
if __name__ == '__main__':
    run()
