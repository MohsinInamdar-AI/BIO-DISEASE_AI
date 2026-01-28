from pydantic import BaseModel, Field
from typing import List, Dict

class PredictRequest(BaseModel):
    dna:str=""
    rna:str=""
    protein: str=""
    top_k:int=Field(default=5,ge=1,le=20)

class TopMatch(BaseModel):
    label:str
    confidence:float

class PredictResponse(BaseModel):
    prediction:str
    confidence:float
    top_matches: List[TopMatch]
    heldout_accuracy:float
