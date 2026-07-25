from datetime import datetime

from pydantic import BaseModel


class HistoryResponse(BaseModel):
    id: int
    url: str
    prediction: str
    created_at: datetime

    class Config:
        from_attributes = True