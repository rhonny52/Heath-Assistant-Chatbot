import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("stopwords")

chatbot = pipeline("text-generation", model="distilgpt2")

def healthcare_chatbot(user_input):
    if "system" in user_input:
        return "Please consult a doctor for accurate advice."
    elif"appointment" in user_input:
        return "Would you like to schedule a appointment with doctor?"
    elif "medication" in user_input:
        return "It's Important to take prerscribed medicine regularly. If you have concerns, consult your doctor"
    else:
        response = chatbot(user_input, max_length=500, num_return_sequences=2)
    return response[0]['generated_text']

def main():
    st.title("Health Assistant Chatbot")

    user_input = st.text_input("How can I help you today?")
    if st.button("Submit"):
        if user_input:
            st.write("User: ", user_input)
            with st.spinner("processing your query, please wait..."):
                response = healthcare_chatbot(user_input)
            st.write("Healthcare Assistant:", response)
            print(response)
        else:
            st.write("Please enter a question.")

if __name__ == "__main__":
    main()
