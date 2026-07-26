def apply_https_rule(features, reasons):
    score = 0

    if not features["uses_https"]:
        score += 1
        reasons.append("URL does not use HTTPS.")

    return score

def apply_ip_rule(features, reasons):
    score = 0

    if features["contains_ip"]:
        score += 2
        reasons.append("URL contains an IP address.")

    return score

def apply_shortener_rule(features, reasons):
    score = 0

    if features["uses_url_shortener"]:
        score += 2
        reasons.append("URL uses a URL shortening service.")

    return score

def apply_at_symbol_rule(features, reasons):
    score = 0

    if features["contains_at_symbol"]:
        score += 2
        reasons.append("URL contains '@'.")

    return score

def apply_hyphen_rule(features, reasons):
    score = 0

    if features["hyphen_count"] >= 2:
        score += 2
        reasons.append("Multiple hyphens detected.")

    return score

def apply_dot_rule(features, reasons):
    score = 0

    if features["dot_count"] >= 4:
        score += 1
        reasons.append("Unusually high number of dots detected.")

    return score

def apply_keyword_rule(features, reasons):
    score = 0

    if features["suspicious_keyword_count"] >= 4:
        score += 3
        reasons.append("Large number of suspicious keywords detected.")
    elif features["suspicious_keyword_count"] >= 2:
        score += 2
        reasons.append("Multiple suspicious keywords detected.")

    return score

RULES = [
    apply_https_rule,
    apply_ip_rule,
    apply_shortener_rule,
    apply_at_symbol_rule,
    apply_hyphen_rule,
    apply_dot_rule,
    apply_keyword_rule,
]

def calculate_confidence(score: int) -> int:
    if score == 0:
        return 100
    elif score == 1:
        return 60
    elif score <= 3:
        return 75
    elif score <= 5:
        return 90
    else:
        return 98

def predict_phishing(features: dict):
    """
    Simple rule-based phishing detection.
    Returns:
        prediction (str)
        confidence (int)
        reasons (list[str])
    """

    score = 0
    reasons = []

    for rule in RULES:
        score += rule(features, reasons)


    if score >= 4:
     prediction = "Phishing"
    elif score >= 1:
        prediction = "Suspicious"
    else:
        prediction = "Safe"

    confidence = calculate_confidence(score)

    return prediction, confidence, reasons