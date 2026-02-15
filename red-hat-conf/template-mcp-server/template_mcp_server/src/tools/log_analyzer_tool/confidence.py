def calculate_confidence(score, total_patterns=3):
    return round(min(score / total_patterns, 1.0), 2)