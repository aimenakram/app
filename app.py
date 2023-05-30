import streamlit as st
import streamlit as st

def display_question(question, options):
    st.write(question)
    for i, option in enumerate(options):
        st.radio(str(i+1), option)

def calculate_score(answers, user_answers):
    score = 0
    for i, ans in enumerate(answers):
        if ans == user_answers[i]:
            score += 1
    return score

# Define the quiz questions and options
questions = [
    "What is the capital of France?",
    "Which planet is known as the Red Planet?",
    "What is the chemical symbol for gold?",
    "What is the largest organ in the human body?",
    "Which country is famous for its kangaroos?"
]

options = [
    ["Paris", "Berlin", "London", "Rome"],
    ["Mars", "Jupiter", "Venus", "Mercury"],
    ["Au", "Ag", "Cu", "Fe"],
    ["Heart", "Brain", "Lungs", "Skin"],
    ["Australia", "Brazil", "India", "Canada"]
]

correct_answers = ["1", "1", "1", "4", "1"]

# Streamlit app
def main():
    st.title("Simple Quiz App")
    st.write("Select the correct option for each question.")

    user_answers = []
    for i in range(len(questions)):
        st.header(f"Question {i+1}")
        display_question(questions[i], options[i])
        user_answer = st.radio("Your answer:", options=[str(j+1) for j in range(len(options[i]))])
        user_answers.append(user_answer)

    score = calculate_score(correct_answers, user_answers)
    st.success(f"Your score: {score}/{len(questions)}")

if __name__ == "__main__":
    main()
