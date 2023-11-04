# app.py
import streamlit as st
import pandas as pd
import os

from src.GemstonePricePrediction.pipelines.prediction_pipeline import PredictPipeline, CustomData
from src.GemstonePricePrediction.utils.utils import load_dataframe, load_object


data = load_dataframe("notebooks/data", "gemstone.csv")
data.drop(['price'], axis=1, inplace=True)

st.write("""
# Gemstone Price Prediction App

This app predicts the **Gemstone Price**!
""")
st.write('---')

# Sidebar
# Header of Specify Input Parameters
st.sidebar.header('Specify Input Parameters')

def user_input_features(data):
    # data = load_dataframe("notebooks/data", "gemstone.csv")
    CARAT = st.sidebar.slider('CARAT', data.carat.min(), data.carat.max(), data.carat.mean())
    DEPTH = st.sidebar.slider('DEPTH', data.depth.min(), data.depth.max(), data.depth.mean())
    TABLE = st.sidebar.slider('TABLE', data.table.min(), data.table.max(), data.table.mean())
    X = st.sidebar.slider('X', data.x.min(), data.x.max(), data.x.mean())
    Y = st.sidebar.slider('Y', data.y.min(), data.y.max(), data.y.mean())
    Z = st.sidebar.slider('Z', data.z.min(), data.z.max(), data.z.mean())
    CUT = st.sidebar.selectbox('CUT', options=['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
    COLOR = st.sidebar.selectbox('COLOR', options=['D', 'E', 'F', 'G', 'H', 'I', 'J'])
    CLARITY = st.sidebar.selectbox('CLARITY', options=['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'])
    data = {'carat': float(CARAT),
            'depth': float(DEPTH),
            'table': float(TABLE),
            'x': float(X),
            'y': float(Y),
            'z': float(Z),
            'cut': str(CUT),
            'color': str(COLOR),
            'clarity': str(CLARITY)
            }
    features = pd.DataFrame(data, index=[0])
    return features


df = user_input_features(data)

# Main Panel

# Print specified input parameters
st.header('Specified Input parameters')
st.write(df)
st.write('---')

predict_pipeline = PredictPipeline()
prediction = predict_pipeline.predict(df)

st.header('Prediction of Gemstone Price')
st.write(prediction)
st.write('---')
