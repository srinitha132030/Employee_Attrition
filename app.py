import streamlit as st
import joblib
import pandas as pd
import numpy as np

model = joblib.load("C:/Users/DELL/OneDrive/Desktop/first.ipynb/project1/attrition_model.pkl")
label_encoder = joblib.load("C:/Users/DELL/OneDrive/Desktop/first.ipynb/project1/label_encoder.pkl")
feature_columns = joblib.load("C:/Users/DELL/OneDrive/Desktop/first.ipynb/project1/feature_columns.pkl")

st.title("Employee Attrition Prediction")
st.markdown("Enter the employee details to predict if they are"
            "likely to leave the company.")
# function to grt user input for prediction
st.sidebar.header("Employee Details")

def get_user_input():
    inputs = {}
    inputs['Age'] = st.sidebar.number_input("Age", min_value=18, max_value=65, value=30)
    inputs['MonthlyIncome'] = st.sidebar.number_input("MonthlyIncome", min_value=1000, max_value=20000, value=5000)
    inputs['JobSatisfaction']=st.sidebar.selectbox("JobSatisfaction",options=[1,2,3,4])
    inputs['OverTime']=st.sidebar.selectbox("OverTime",options=["Yes","No"])
    inputs['DistanceFromHome']=st.sidebar.number_input("DistanceFromHome",min_value=0,max_value=50,value=10)
    
    data = {}
    for feat in feature_columns:
        if feat in inputs:
            data[feat] = inputs[feat]
        else:
            data[feat] = 0
        return pd.DataFrame(data, index=[0])
user_input = get_user_input()

user_input=get_user_input()
user_input['OverTime']=label_encoder.transform(user_input['OverTime'])

#Predict the attribution
if st.button("Predict Attribution"):
    prediction = model.predict(user_input)
    if prediction[0]==1:
        st.error("The employee is likely to leave the company.")
    else:
        st.success("The employee is likely to stay with the company.")
    st.info(f"Prediction Probability:{probability:.2f}")





