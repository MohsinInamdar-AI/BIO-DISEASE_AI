def combine_sequences(dna: str, rna: str, protein: str) -> str:
    dna = (dna or "").strip().upper()
    rna = (rna or "").strip().upper()
    protein = (protein or "").strip().upper()
    return f"DNA_{dna} RNA_{rna} PROT_{protein}"
