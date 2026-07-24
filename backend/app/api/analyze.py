from fastapi import APIRouter

from backend.app.utils.url_features import extract_url_features

router = APIRouter()


@router.get("/analyze")
def analyze_url(url: str):
    """
    Analyze a URL and return extracted features.
    """
    return extract_url_features(url)