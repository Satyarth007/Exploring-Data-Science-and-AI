import re

RULES = {
    "OutOfMemory": [r"outofmemory", r"oom", r"killed process"],
    "CrashLoop": [r"crashloopbackoff"],
    "ConnectionRefused": [r"connection refused"],
    "Timeout": [r"timed?\s*out"],
    "PermissionDenied": [r"permission denied"],
    "DiskFull": [r"no space left", r"disk full"]
}

def match_rules(text):
    matches = {}
    for issue, patterns in RULES.items():
        score = 0
        for p in patterns:
            if re.search(p, text, re.IGNORECASE):
                score += 1
        if score:
            matches[issue] = score
    return matches