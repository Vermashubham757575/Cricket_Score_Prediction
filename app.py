import streamlit as st
import pandas as pd
import joblib
import numpy as np
import sklearn 
from sklearn.neighbors import KNeighborsRegressor


model = joblib.load("KNN.pkl")

# Streamlit UI elements
st.title("IPL Score Prediction App")

# User input fields
bat_team = st.selectbox("Batting Team", [
    'Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab', 
    'Kolkata Knight Riders', 'Mumbai Indians', 'Rajasthan Royals',
    'Royal Challengers Bangalore', 'Sunrisers Hyderabad'])

bowl_team = st.selectbox("Bowling Team", [
    'Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab', 
    'Kolkata Knight Riders', 'Mumbai Indians', 'Rajasthan Royals',
    'Royal Challengers Bangalore', 'Sunrisers Hyderabad'])

overs = st.number_input("Overs", 5.0, 20.0, 5.0)
runs = st.number_input("Runs", 0, 500, 50)
wickets = st.number_input("Wickets", 0, 10, 2)
runs_last_5 = st.number_input("Runs in Last 5 Overs", 0, 100, 20)
wickets_last_5 = st.number_input("Wickets in Last 5 Overs", 0, 10, 1)

# Encode the selected batting and bowling teams
bat_team_encoded = [0] * 8
bowl_team_encoded = [0] * 8

bat_team_encoded[
    ['Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab', 
    'Kolkata Knight Riders', 'Mumbai Indians', 'Rajasthan Royals',
    'Royal Challengers Bangalore', 'Sunrisers Hyderabad'].index(bat_team)
] = 1

bowl_team_encoded[
    ['Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab', 
    'Kolkata Knight Riders', 'Mumbai Indians', 'Rajasthan Royals',
    'Royal Challengers Bangalore', 'Sunrisers Hyderabad'].index(bowl_team)
] = 1

# Create a DataFrame for prediction
input_data = np.array([
    bat_team_encoded + bowl_team_encoded + [overs, runs, wickets, runs_last_5, wickets_last_5]
])

# Make prediction when the "Predict" button is clicked
# Make prediction when the "Predict" button is clicked
if st.button("Predict"):
    prediction = model.predict(input_data)
    predicted_score = int(prediction[0])  # Convert the float prediction to an integer
    st.subheader(f"Predicted Score: {predicted_score} runs")

