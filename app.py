import streamlit as st
import formulas

def main():
    st.title("Hello, well come to the super stuped macro calculator!")
    st.write("This is a simple macro calculator that will help you calculate your daily macronutrient needs based on your goals and activity level.")
    weight = st.number_input("Enter your weight in kg:")
    height = st.number_input("Enter your height in cm:")
    age = st.number_input("Enter your age:")
    sex = st.selectbox("Select your sex:", ["Male", "Female"])
    activity_level = st.selectbox("Select your activity level:", ["Sedentary (little or no exercise)", "Slightly active (exercise 1-3 days/week)", "Moderately active (exercise 3-5 days/week)", "Active (exercise 6-7 days/week)", "Super active (very hard exercise & physical job or 2x training)"])
    goal = st.selectbox("Select your goal:", ["Lose weight", "Maintain weight", "Gain weight"])
    if st.button("Calculate"):
        tbm_result = formulas.tbm(sex.lower()[0], age, weight, height)
        get_result = formulas.get(tbm_result, activity_level)
        calories_result = formulas.calories(get_result, goal)
        formulas.macros(calories_result, goal, weight)
        st.write('TMB:', tbm_result)
        st.write('GET:', get_result)
        st.write('Calories:', calories_result)