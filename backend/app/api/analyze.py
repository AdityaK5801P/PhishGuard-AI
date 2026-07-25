from fastapi import APIRouter

from backend.app.schemas.analyze import AnalyzeRequest, AnalyzeResponse
from backend.app.utils.url_features import extract_url_features

router = APIRouter()


@router.post("/analyze", response_model=AnalyzeResponse)
def analyze_url(request: AnalyzeRequest):
    """
    Analyze a URL and return extracted features.
    """

    features = extract_url_features(str(request.url))

    return AnalyzeResponse(
        status="success",
        prediction="Unknown",
        features=features,
    )