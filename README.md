# 🩺 Gemini Medical Q&A

A Streamlit web application that uses Google's Gemini AI (`gemini-1.5-flash`) to answer **medical-related questions only**. It filters queries to ensure relevance and safety, providing intelligent responses through a simple UI.

---

## 🚀 Features

- ✅ Streamlit-based web interface
- ✅ Integrates with Google Generative AI (Gemini)
- ✅ Filters to process only medical-related questions
- ✅ User-friendly text input and response display
- ⚠️ Responds with a warning for non-medical queries

---

## 🛠️ Installation

1. **Clone the repository**:

```bash
git clone https://github.com/JagannathM05/-Gemini-Medical-Q-A.git
cd -Gemini-Medical-Q-A
````

2. **(Optional)** Create and activate a virtual environment:

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Add your API key**:

Create a `.env` file in the root directory and paste:

```
GOOGLE_API_KEY=your_api_key_here
```

> Replace `your_api_key_here` with your actual Gemini API key from Google.

---

## ▶️ Running the App

Start the app using:

```bash
streamlit run Med_app.py
```

The app will launch in your browser. Ask any medical question and get answers powered by Gemini AI.

---

## 📁 Project Structure

```
.
├── Med_app.py            # Main Streamlit application
├── requirements.txt      # Python dependencies
└── .env                  # Environment file with API key (you create this)
```

---

## 📌 Notes

* This app is for **educational/demo purposes** and does **not provide professional medical advice**.
* Ensure your `.env` file is added to `.gitignore` to avoid exposing your API key.
* The app uses the **Gemini 1.5 Flash model** for balanced performance.
