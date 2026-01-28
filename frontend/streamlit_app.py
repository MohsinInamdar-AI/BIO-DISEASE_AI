import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Page config
# -------------------------------
st.set_page_config(
    page_title="BioSequence Disease Risk Predictor",
    layout="wide"
)

st.title("🧬 BioSequence Disease Risk Predictor")
st.caption("Predict disease risk from DNA / RNA / Protein sequences")

# -------------------------------
# API URL input
# -------------------------------
API_BASE = st.text_input(
    "FastAPI URL",
    value="http://127.0.0.1:8000"
)

st.markdown("---")

# -------------------------------
# Input section
# -------------------------------
st.subheader("Input Sequences")

col1, col2, col3 = st.columns(3)

with col1:
    dna = st.text_area("DNA (ACGT)", height=120)

with col2:
    rna = st.text_area("RNA (ACGU)", height=120)

with col3:
    protein = st.text_area("Protein (Amino acids)", height=120)

top_k = st.slider("Top-K Predictions", min_value=3, max_value=10, value=5)

# -------------------------------
# Predict button
# -------------------------------
if st.button("🔍 Predict Disease", use_container_width=True):
    payload = {
        "dna": dna,
        "rna": rna,
        "protein": protein,
        "top_k": top_k
    }

    try:
        response = requests.post(
            API_BASE.rstrip("/") + "/predict",
            json=payload,
            timeout=60
        )
    except Exception as e:
        st.error(f"Cannot connect to backend: {e}")
        st.stop()

    if response.status_code != 200:
        st.error(response.text)
        st.stop()

    out = response.json()

    # -------------------------------
    # Results section
    # -------------------------------
    st.markdown("---")
    st.subheader("Prediction Result")

    st.success(
        f"🩺 **Predicted Disease:** {out['prediction']}  "
        f"|  **Confidence:** {out['confidence']:.4f}"
    )

    st.write(
        f"📊 **Model held-out accuracy:** {out['heldout_accuracy']:.4f}"
    )

    # -------------------------------
    # Confidence bar chart
    # -------------------------------
    st.markdown("### 🔐 Prediction Confidence")

    fig, ax = plt.subplots()
    ax.bar(["Confidence"], [out["confidence"]])
    ax.set_ylim(0, 1)
    ax.set_ylabel("Probability")

    st.pyplot(fig, clear_figure=True)

    # -------------------------------
    # Top-K probabilities table
    # -------------------------------
    st.markdown("### 🧾 Top-K Predictions")

    top_df = pd.DataFrame(out["top_matches"])
    st.dataframe(top_df, use_container_width=True)

    # -------------------------------
    # Top-K probability graph
    # -------------------------------
    st.markdown("### 📊 Top-K Probability Distribution")

    labels = top_df["label"].tolist()
    values = top_df["confidence"].tolist()

    fig, ax = plt.subplots()
    ax.barh(labels[::-1], values[::-1])
    ax.set_xlim(0, 1)
    ax.set_xlabel("Probability")

    st.pyplot(fig, clear_figure=True)

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.caption("End-to-end ML system | FastAPI + Scikit-learn + Streamlit")
