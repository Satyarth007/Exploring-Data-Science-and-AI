from .parser import parse_logs
from .detector import detect_issues
from .severity import get_severity
from .fixes import get_fix
from .confidence import calculate_confidence


def analyze_logs(raw_logs: str):

    lines = parse_logs(raw_logs)
    detected = detect_issues(lines)
    results = []

    for issue, score in detected.items():
        results.append({
            "issue": issue,
            "severity": get_severity(issue),
            "confidence": calculate_confidence(score),
            "suggested_fix": get_fix(issue)
        })

    return {
        "total_issues": len(results),
        "analysis": sorted(results, key=lambda x: x["confidence"], reverse=True)
    }

if __name__ == "__main__":
    sample = "connection refused to database\nDisk full error detected"
    print(analyze_logs(sample))