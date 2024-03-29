# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 19:43:55 2024

@author: Xabit
"""

import pickle
import numpy as np
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
from sklearn.preprocessing import StandardScaler
 
scaler = StandardScaler()
df = pd.read_csv('diabetes.csv')
x = df.drop(columns='Outcome', axis=1)
y = df['Outcome']
scaler.fit(x)
standardized_data = scaler.transform(x)
diabetes_model = pickle.load(open('diabetes_model.sav','rb'))
with st.sidebar:
    selected = option_menu('DIABETE Disease Pred',
                    ['Diabetes Prediction', 'GFR','About the Diab'],
                    default_index = 0)
    
    
    
if (selected == 'Diabetes Prediction' ):
    
    st.title('Diabetes Prediction with ML')
    Pregnancies = st.text_input('Preg')
    Glucose = st.text_input('Gluco')
    BloodPressure = st.text_input('Blood Pres')
    SkinThickness = st.text_input('SkinThick')
    Insulin = st.text_input('Insul')
    BMI = st.text_input('BMI')
    DiabetesPedigreeFunction = st.text_input('DiabPedi')
    Age = st.text_input('Age')
    
    # code for pred
    
    diab_dignosis = ''
    
    #creatint button for prediction
    
    if st.button('Diabetes Test Result'):
        input_data = [[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]]
        input_data_array = np.asarray(input_data)

        #reshape
        input_data_reshaped = input_data_array.reshape(1,-1)
        std_data = scaler.transform(input_data_reshaped)
        
        diab_prediction = diabetes_model.predict(std_data)
        
        if(diab_prediction >= 0.5):
            diab_dignosis = ' Diabetic'
        else:
            diab_dignosis = 'not Diabetic'
    st.success(diab_dignosis)

