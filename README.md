
# 🧬 BioSequence Disease Risk Predictor

An industry-style end-to-end Machine Learning project that predicts disease risk from DNA, RNA, and Protein sequences.

---

## 🚀 Project Overview

**Goal:** Predict disease categories (cancer, normal, metabolic, neurological) from biological sequences.

This project demonstrates:
- Feature engineering on genomic sequences
- Model training and evaluation
- Production-style API deployment
- Interactive frontend visualization

---

## 🏗️ Architecture

User → Streamlit Frontend → FastAPI Backend → ML Model

---

## 📁 Project Structure

```
bio-disease-ai/
├── main.py
├── model.py
├── schemas.py
├── utils.py
├── models/
│   ├── disease_model.joblib
│   └── metrics.joblib
├── training/
│   ├── train_model.py
│   └── dataset.csv
├── frontend/
│   └── streamlit_app.py
├── requirements.txt
└── README.md
```

---

## 🧠 Machine Learning

- TF-IDF (character n-grams)
- Logistic Regression
- Probability-based predictions

---

## 📊 Evaluation

- Train/Test split
- Accuracy, Precision, Recall, F1-score
- Top-K probability analysis

---

## 🌐 API Endpoints

### Health
GET /health

### Predict
POST /predict

---

## ▶️ How to Run

1. Install dependencies  
   `pip install -r requirements.txt`

2. Train model  
   `python training/train_model.py`

3. Start backend  
   `uvicorn main:app --reload`

4. Start frontend  
   `streamlit run frontend/streamlit_app.py`

---

## 💼 Resume Description

Built an end-to-end bioinformatics ML system using FastAPI and Streamlit to predict disease risk from genomic sequences.

---

## 📜 License

Educational use.
