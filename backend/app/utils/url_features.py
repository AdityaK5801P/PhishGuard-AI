from urllib.parse import urlparse


def extract_url_features(url: str) -> dict:
    """
    Extract basic security-related features from a URL.
    """

    parsed_url = urlparse(url)

    features = {
        "url": url,
        "url_length": len(url),
        "scheme": parsed_url.scheme,
        "domain": parsed_url.netloc,
        "path": parsed_url.path,
        "uses_https": parsed_url.scheme.lower() == "https",
        "contains_ip": False,      # We'll implement this later
        "contains_at_symbol": "@" in url,
        "hyphen_count": url.count("-"),
        "dot_count": url.count("."),
    }

    return features