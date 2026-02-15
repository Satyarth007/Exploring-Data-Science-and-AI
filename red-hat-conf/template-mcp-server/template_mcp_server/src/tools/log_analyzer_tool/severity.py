SEVERITY_LEVELS = {
    "OutOfMemory": "CRITICAL",
    "DiskFull": "CRITICAL",
    "CrashLoop": "HIGH",
    "PermissionDenied": "MEDIUM",
    "ConnectionRefused": "MEDIUM",
    "Timeout": "LOW",
    "Unknown": "UNKNOWN"
}

def get_severity(issue):
    return SEVERITY_LEVELS.get(issue, "UNKNOWN")