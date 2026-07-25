from sqlalchemy.orm import Session

from backend.app.database.models import Scan
from backend.app.utils.url_features import extract_url_features


def analyze_and_save_url(db: Session, url: str):
    """
    Analyze a URL, save the scan to the database,
    and return the extracted features.
    """

    features = extract_url_features(url)

    prediction = "Unknown"

    scan = Scan(
        url=url,
        prediction=prediction,
        uses_https=features["uses_https"],
        contains_ip=features["contains_ip"],
        contains_at_symbol=features["contains_at_symbol"],
        hyphen_count=features["hyphen_count"],
        dot_count=features["dot_count"],
    )

    db.add(scan)
    db.commit()
    db.refresh(scan)

    return prediction, features