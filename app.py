import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open('churn_model.pkl', 'rb'))

st.title('Customer Churn Predictor')
st.write('Enter customer details below to predict churn')

tenure = st.number_input('Tenure in Months', min_value=0, max_value=100, value=12)
monthly_charges = st.number_input('Monthly Charges', min_value=0.0, max_value=200.0, value=50.0)
total_charges = st.number_input('Total Charges', min_value=0.0, max_value=10000.0, value=600.0)
contract = st.selectbox('Contract Type', [0, 1, 2], format_func=lambda x: ['Month to Month', 'One Year', 'Two Year'][x])
paperless = st.selectbox('Paperless Billing', [0, 1], format_func=lambda x: ['No', 'Yes'][x])
payment = st.selectbox('Payment Method', [0, 1, 2, 3], format_func=lambda x: ['Bank Transfer', 'Credit Card', 'Electronic Check', 'Mailed Check'][x])
senior = st.selectbox('Senior Citizen', [0, 1], format_func=lambda x: ['No', 'Yes'][x])
partner = st.selectbox('Has Partner', [0, 1], format_func=lambda x: ['No', 'Yes'][x])
dependents = st.selectbox('Has Dependents', [0, 1], format_func=lambda x: ['No', 'Yes'][x])
phone = st.selectbox('Phone Service', [0, 1], format_func=lambda x: ['No', 'Yes'][x])
internet = st.selectbox('Internet Service', [0, 1, 2], format_func=lambda x: ['DSL', 'Fiber Optic', 'No'][x])

if st.button('Predict Churn'):
    features = pd.DataFrame([[senior, partner, dependents, tenure,
                              phone, internet, paperless, payment,
                              monthly_charges, total_charges, contract]],
                            columns=['SeniorCitizen', 'Partner', 'Dependents',
                                    'tenure', 'PhoneService', 'InternetService',
                                    'PaperlessBilling', 'PaymentMethod',
                                    'MonthlyCharges', 'TotalCharges', 'Contract'])
    prediction = model.predict(features)
    if prediction[0] == 1:
        st.error('This customer is likely to churn')
    else:
        st.success('This customer is not likely to churn') #download app.py

