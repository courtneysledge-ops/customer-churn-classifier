
import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load model and feature list
model_data = pickle.load(open('churn_model.pkl', 'rb'))
model = model_data['model']
feature_columns = model_data['features']

st.title('Customer Churn Predictor')
st.write('Enter customer details below')

tenure = st.number_input('Tenure in Months', min_value=0, max_value=100, value=12)
monthly_charges = st.number_input('Monthly Charges', min_value=0.0, max_value=200.0, value=50.0)
total_charges = st.number_input('Total Charges', min_value=0.0, max_value=10000.0, value=600.0)

if st.button('Predict Churn'):
    # Create a row of zeros for all features
    input_data = pd.DataFrame([np.zeros(len(feature_columns))], columns=feature_columns)
   
    # Fill in the values we have
    input_data['tenure'] = tenure
    input_data['MonthlyCharges'] = monthly_charges
    input_data['TotalCharges'] = total_charges
   
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error('This customer is likely to churn')
    else:
        st.success('This customer is not likely to churn')
#save app.py
