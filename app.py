
import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('churn_model.pkl', 'rb'))

st.title('Customer Churn Predictor')
st.write('Enter customer details below to predict churn')

tenure = st.number_input('Tenure in Months', min_value=0, max_value=100, value=12)
monthly_charges = st.number_input('Monthly Charges', min_value=0.0, max_value=200.0, value=50.0)
total_charges = st.number_input('Total Charges', min_value=0.0, max_value=10000.0, value=600.0)
contract = st.selectbox('Contract Type', [0, 1, 2], format_func=lambda x: ['Month to Month', 'One Year', 'Two Year'][x])

if st.button('Predict Churn'):
    features = np.array([[tenure, monthly_charges, total_charges, contract]])
    prediction = model.predict(features)
    if prediction[0] == 1:
        st.error('This customer is likely to churn')
    else:
        st.success('This customer is not likely to churn')
#download app.py
