import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "disease_model.joblib"
METRICS_PATH = BASE_DIR / "models" / "metrics.joblib"

if not MODEL_PATH.exists() or not METRICS_PATH.exists():
        raise FileNotFoundError("Run training/train_model.py first to generate model files.")

model = joblib.load(MODEL_PATH)
metrics = joblib.load(METRICS_PATH)

