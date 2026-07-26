from pydantic import BaseModel, HttpUrl


class AnalyzeRequest(BaseModel):
    url: HttpUrl


class AnalyzeResponse(BaseModel):
    status: str
    prediction: str
    confidence: int
    reasons: list[str]
    features: dict