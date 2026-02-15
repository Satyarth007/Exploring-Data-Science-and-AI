from .rules import match_rules

def detect_issues(lines):
    joined = " ".join(lines)
    matches = match_rules(joined)
    if not matches:
        return {"Unknown": 1}
    return matches