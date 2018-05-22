import re

def validate(text):
    if re.search(r'<(|\/|[^\/>][^>]+|\/[^>][^>]+)>',text):
        return False
    return True