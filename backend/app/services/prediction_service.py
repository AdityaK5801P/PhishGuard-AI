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

    if not features["uses_https"]:
        score += 1
        reasons.append("URL does not use HTTPS.")

    if features["contains_ip"]:
        score += 2
        reasons.append("URL contains an IP address.")

    if features["contains_at_symbol"]:
        score += 2
        reasons.append("URL contains '@'.")

    if features["hyphen_count"] >= 2:
        score += 1
        reasons.append("Multiple hyphens detected.")

    if features["dot_count"] >= 4:
        score += 1
        reasons.append("Large number of dots detected.")

    if score >= 4:
        prediction = "Phishing"
        confidence = 95
    elif score >= 2:
        prediction = "Suspicious"
        confidence = 75
    else:
        prediction = "Safe"
        confidence = 98

    return prediction, confidence, reasons