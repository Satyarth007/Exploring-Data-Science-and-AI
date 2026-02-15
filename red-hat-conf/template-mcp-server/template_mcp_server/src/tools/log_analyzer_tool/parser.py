import json

def parse_logs(raw_logs):
    lines = raw_logs.strip().split("\n")
    parsed = []
    for line in lines:
        line=line.strip()
        try:
            obj=json.loads(line)
            parsed.append(str(obj))
        except:
            parsed.append(line)
    return parsed