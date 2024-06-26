import streamlit as st
from mcq_generator import generate_mcqs

def streamlit_app():
    st.title("MCQ Generator")

    text_input = st.text_area("Enter your text here:")
    if st.button("Generate MCQs"):
        if text_input:
            mcqs = generate_mcqs(text_input)
            for i, mcq in enumerate(mcqs, 1):
                st.subheader(f"Question {i}")
                st.write(mcq['question'])
                options = [mcq['answer']] + mcq['distractors']
                st.radio("Choose the correct answer:", options, key=f"q{i}")
        else:
            st.warning("Please enter some text to generate MCQs.")

if __name__ == "__main__":
    streamlit_app()
