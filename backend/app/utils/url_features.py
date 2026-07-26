from urllib.parse import urlparse
import ipaddress
SUSPICIOUS_KEYWORDS = [
    "login",
    "verify",
    "secure",
    "account",
    "password",
    "update",
    "bank",
    "signin",
]


def extract_url_features(url: str) -> dict:
    """
    Extract basic security-related features from a URL.
    """

    parsed_url = urlparse(url)

    hostname = parsed_url.hostname or ""

    try:
        ipaddress.ip_address(hostname)
        contains_ip = True
    except ValueError:
        contains_ip = False

    url_lower = url.lower()
    matched_keywords = [
    keyword
    for keyword in SUSPICIOUS_KEYWORDS
    if keyword in url_lower
]

    features = {
        "url": url,
        "url_length": len(url),
        "scheme": parsed_url.scheme,
        "domain": parsed_url.netloc,
        "path": parsed_url.path,
        "uses_https": parsed_url.scheme.lower() == "https",
        "contains_ip": contains_ip,
        "contains_at_symbol": "@" in url,
        "hyphen_count": url.count("-"),
        "dot_count": url.count("."),
        "suspicious_keywords": matched_keywords,
        "suspicious_keyword_count": len(matched_keywords),
    }

    return features