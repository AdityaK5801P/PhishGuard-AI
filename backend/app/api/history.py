from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.database.database import get_db
from backend.app.schemas.history import HistoryResponse
from backend.app.services.history_service import get_scan_history

router = APIRouter()


@router.get("/history", response_model=List[HistoryResponse])
def history(db: Session = Depends(get_db)):
    return get_scan_history(db)