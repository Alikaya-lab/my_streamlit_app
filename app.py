import streamlit as st

st.title("FitFast AI MVP")

st.write("Welcome to FitFast AI")

goal = st.selectbox("Choose your goal", ["Fat Loss", "Muscle Gain"])

if st.button("Generate Workout"):

    if goal == "Fat Loss":
        workout = ["Jump rope 10 min", "Pushups 3x12", "Squats 3x15"]
    else:
        workout = ["Pullups 4x8", "Bench Press 4x10", "Deadlift 3x8"]

    st.write("Your workout plan:")
    st.write(workout)