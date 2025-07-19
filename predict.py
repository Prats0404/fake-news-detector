import pickle

# Load the model and vectorizer
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Take input
news_text = input("Enter the news article text:\n")

# Transform and predict
vectorized_input = vectorizer.transform([news_text])
prediction = model.predict(vectorized_input)

# Output result
if prediction[0] == 0:
    print("\n🔴 This news article is FAKE.")
else:
    print("\n🟢 This news article is REAL.")
