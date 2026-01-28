from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .schemas import PredictRequest, PredictResponse
from .model import model, metrics
from .utils import combine_sequences

app = FastAPI(title="BioSequence Disease Risk API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "running", "heldout_accuracy": metrics.get("heldout_accuracy", None)}

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    combined = combine_sequences(req.dna, req.rna, req.protein)

    if combined.strip() == "DNA_ RNA_ PROT_":
        raise HTTPException(status_code=400, detail="Provide at least one of DNA/RNA/Protein.")

    proba = model.predict_proba([combined])[0]
    classes = model.classes_

    k = int(req.top_k)
    top_idx = proba.argsort()[::-1][:k]
    top = [{"label": classes[i], "confidence": float(proba[i])} for i in top_idx]

    return {
        "prediction": top[0]["label"],
        "confidence": float(top[0]["confidence"]),
        "top_matches": top,
        "heldout_accuracy": float(metrics.get("heldout_accuracy", 0.0)),
    }