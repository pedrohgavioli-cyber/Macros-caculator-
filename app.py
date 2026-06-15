import streamlit as st
import formulas

def main():
    st.title("Welcome to the Macro Calculator! 🍎")
    st.write("This is a simple macro calculator that will help you calculate your daily macronutrient needs based on your goals and activity level.")

    col1, col2, col3 = st.columns(3)
    with col1:
        weight = st.number_input("Weight (kg):", min_value=1.0, value=70.0, step=0.1)
    with col2:
        height = st.number_input("Height (cm):", min_value=50.0, value=170.0, step=1.0)
    with col3:
        age = st.number_input("Age (years):", min_value=1, value=30, step=1)

    sex_option = st.selectbox("Select your sex:", ["Male", "Female"])
    sex = 'm' if sex_option == "Male" else 'f'

    activity_options = {
        "Sedentary (little or no exercise)": 1,
        "Slightly active (exercise 1-3 days/week)": 2,
        "Moderately active (exercise 3-5 days/week)": 3,
        "Active (exercise 6-7 days/week)": 4,
        "Super active (very hard exercise & physical job or 2x training)": 5
    }
    activity_level_str = st.selectbox("Select your activity level:", list(activity_options.keys()))
    activity_level = activity_options[activity_level_str]

    goal_options = {
        "Lose weight": 1,
        "Maintain weight": 2,
        "Gain weight": 3
    }
    goal_str = st.selectbox("Select your goal:", list(goal_options.keys()))
    goal = goal_options[goal_str]

    if st.button("Calculate Macros 🚀"):
        tbm_result = formulas.tbm(sex, age, weight, height)
        get_result = formulas.get(tbm_result, activity_level)
        calories_result = formulas.calories(get_result, goal)

        st.subheader("Your Results 📊")
        st.write(f"**TBM (Basal Metabolic Rate):** {tbm_result:.0f} kcal")
        st.write(f"**GET (Total Energy Expenditure):** {get_result:.0f} kcal")
        st.write(f"**Target Calories:** {calories_result:.0f} kcal")

        macros_result = formulas.macros(calories_result, goal, weight)
        if macros_result:
            protein, carbs, fats, fiber = macros_result
            st.write("### Macronutrients")
            mcol1, mcol2, mcol3, mcol4 = st.columns(4)
            mcol1.metric("Protein", f"{protein:.0f}g")
            mcol2.metric("Carbs", f"{carbs:.0f}g")
            mcol3.metric("Fats", f"{fats:.0f}g")
            mcol4.metric("Fiber", f"{fiber:.0f}g")

if __name__ == "__main__":
    main()
