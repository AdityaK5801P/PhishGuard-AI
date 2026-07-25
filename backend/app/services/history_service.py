from sqlalchemy.orm import Session

from backend.app.database.models import Scan


def get_scan_history(db: Session):
    """
    Return all scans ordered by newest first.
    """
    return (
        db.query(Scan)
        .order_by(Scan.created_at.desc())
        .all()
    )