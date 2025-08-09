# 📰 Fake News Detector using Machine Learning

A machine learning-powered web app built with Streamlit that accurately detects whether a given news article is **real** or **fake**. This project uses a Logistic Regression model trained on a labeled dataset of news articles.

---

## 🔍 Features

- Classifies news articles as **Fake** or **Real**
- Easy-to-use Streamlit web interface
- High accuracy (~98.5%)
- Clean and reusable Python code
- Hosted locally for quick testing

---

## 🛠️ Tech Stack

| Area        | Tools / Libraries                     |
|-------------|----------------------------------------|
| Language    | Python 3.10                            |
| Libraries   | Pandas, NumPy, Scikit-learn, Streamlit |
| ML Model    | Logistic Regression                    |
| Vectorizer  | TF-IDF (Term Frequency-Inverse Document Frequency) |
| IDE         | VS Code                                |

## 📁 Project Structure
📦 fake-news-detector/
│
├── Dataset/
│ ├── True.csv
│ └── Fake.csv
│
├── model.pkl # Trained ML model
├── vectorizer.pkl # TF-IDF vectorizer
├── app.py # Streamlit web application
├── predict.py # Contains prediction logic
├── requirements.txt # List of required Python packages
├── README.md # This file
└── fake_news_detector.ipynb # Jupyter Notebook (model building)

## 🚀 How to Run Locally

1. **Clone the Repository**

```bash
git clone https://github.com/Prats0404/fake-news-detector.git
cd fake-news-detector

2.Create & Activate Virtual Environment (Optional but Recommended)
python -m venv myenv
myenv\Scripts\activate  # On Windows

3.Install Dependencies
pip install -r requirements.txt

4.Run the Streamlit App
streamlit run app.py
The app will open in your default browser at http://localhost:8501

📊 Model Accuracy

    Accuracy: 98.54%

    Precision: 0.98–0.99

    Recall: 0.98–0.99

    F1-Score: 0.98–0.99


🙋‍♂️ Author
Prathvi V Suvarna
📧 prathvisvrna@gmail.com
🌐 LinkedIn
💻 GitHub
📌 License
This project is for educational purposes. No license added yet.
If you found this project helpful, please consider starring ⭐ it on GitHub!

### ✅ Want Me to Help Add This to Your Resume?
Just say: **"Add this project to my resume"**, and I’ll write a bullet point for you.

Or ready for the **next project suggestion**? Let me know!



