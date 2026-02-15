FIXES = {
    "OutOfMemory": "Increase memory or optimize application usage.",
    "CrashLoop": "Check container logs and startup configuration.",
    "ConnectionRefused": "Ensure service is running and port is correct.",
    "Timeout": "Check network latency and service health.",
    "PermissionDenied": "Verify file or user permissions.",
    "DiskFull": "Free disk space or increase storage.",
    "Unknown": "No fix available."
}

def get_fix(issue):
    return FIXES.get(issue, "No fix available.")