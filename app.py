import streamlit as st
import pickle

st.set_page_config(page_title="Fake News Detector", layout="centered")

# Load model and vectorizer
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

st.title("📰 Fake News Detector")
st.write("Enter a news article below and click Predict to check if it's real or fake.")

input_text = st.text_area("Enter a news article or headline:")

if st.button("Predict"):
    if input_text.strip() != "":
        vectorized = vectorizer.transform([input_text])
        result = model.predict(vectorized)[0]
        if result == 0:
            st.error("🚨 This looks like *Fake News*.")
        else:
            st.success("✅ This seems like *Real News*.")
    else:
        st.warning("Please enter some text before clicking Predict.")
