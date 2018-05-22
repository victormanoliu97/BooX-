import re

def validate(textToCheck):
    pattern = re.compile(r"('(''|[^'])*')|(;)|(\b(ALTER|CREATE|DELETE|DROP|EXEC(UTE){0,1}|INSERT( +INTO){0,1}|MERGE|SELECT|UPDATE|UNION( +ALL){0,1})\b)  ")

    if (pattern.match(textToCheck)) or (re.findall(pattern, textToCheck)):
        return False
    else:
        return True




