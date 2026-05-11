import os
import json
import re

with open(r'f:\conrutas\AppBeluso\src\data\pois.ts', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if '"description":' in line:
        # Extract the content between the first and last double quote in the value part
        parts = line.split('"description":', 1)
        prefix = parts[0] + '"description":'
        value_part = parts[1].strip()
        
        # Find the first and last quote
        first_quote = value_part.find('"')
        last_quote = value_part.rfind('"')
        
        if first_quote != -1 and last_quote != -1 and first_quote != last_quote:
            content = value_part[first_quote+1:last_quote]
            # Escape all double quotes inside the content
            escaped_content = content.replace('"', '\\"')
            line = prefix + ' "' + escaped_content + '",\n'
    new_lines.append(line)

with open(r'f:\conrutas\AppBeluso\src\data\pois.ts', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Escaped quotes in pois.ts successfully using line-by-line approach")
