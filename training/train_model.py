import pandas as pd
import joblib
from pathlib import Path
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

ROOT = Path(__file__).resolve().parent.parent
MODEL_DIR = ROOT / "backend" / "models"
MODEL_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(Path(__file__).resolve().parent /r"D:\My all projects\bio-disease-ai\docs\genomic_disease_dataset.csv")
df.columns = [c.lower() for c in df.columns]

# Combine sequences into one text string (same style as your existing project)
df["combined"] = (
    "DNA_" + df["dna"].astype(str).str.upper()
    + " RNA_" + df["rna"].astype(str).str.upper()
    + " PROT_" + df["protein"].astype(str).str.upper()
)

X_train, X_test, y_train, y_test = train_test_split(
    df["combined"], df["disease"],
    test_size=0.25, random_state=42, stratify=df["disease"] if df["disease"].nunique() > 1 else None
)

model = Pipeline([
    ("tfidf", TfidfVectorizer(analyzer="char", ngram_range=(4, 6), min_df=1)),
    ("clf", LogisticRegression(max_iter=2000))
])

model.fit(X_train, y_train)
pred = model.predict(X_test)

acc = float(accuracy_score(y_test, pred))
print("Held-out accuracy:", acc)
print(classification_report(y_test, pred, zero_division=0))

joblib.dump(model, MODEL_DIR / "disease_model.joblib")
joblib.dump({"heldout_accuracy": acc}, MODEL_DIR / "metrics.joblib")

print("Saved model artifacts to:", MODEL_DIR)
