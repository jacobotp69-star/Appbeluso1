import os
import json
import re

with open(r'f:\conrutas\AppBeluso\src\data\pois.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find double quotes inside the description string
# We need to escape any " that is NOT preceded by : and NOT followed by ,
# But simpler: just find the description value and escape all " inside it except the start and end ones.

def escape_quotes_in_desc(match):
    prefix = match.group(1)
    desc_content = match.group(2)
    suffix = match.group(3)
    # Escape unescaped double quotes
    # But be careful not to escape already escaped ones
    escaped_content = desc_content.replace('"', '\\"')
    return f'{prefix}{escaped_content}{suffix}'

# Match "description": "..."
pattern = r'("description":\s*")(.*?)(")'
new_content = re.sub(pattern, escape_quotes_in_desc, content, flags=re.DOTALL)

with open(r'f:\conrutas\AppBeluso\src\data\pois.ts', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Escaped quotes in pois.ts successfully")
