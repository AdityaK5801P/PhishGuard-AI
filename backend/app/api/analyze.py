from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.database.database import get_db
from backend.app.schemas.analyze import AnalyzeRequest, AnalyzeResponse
from backend.app.services.analyzer_service import analyze_and_save_url

router = APIRouter()


@router.post("/analyze", response_model=AnalyzeResponse)
def analyze_url(
    request: AnalyzeRequest,
    db: Session = Depends(get_db),
):
    prediction, features = analyze_and_save_url(
        db=db,
        url=str(request.url),
    )

    return AnalyzeResponse(
        status="success",
        prediction=prediction,
        features=features,
    )