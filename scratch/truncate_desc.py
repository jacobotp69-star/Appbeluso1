import os
import re

with open(r'f:\conrutas\AppBeluso\src\data\pois.ts', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if '"description":' in line:
        parts = line.split('"description":', 1)
        prefix = parts[0] + '"description":'
        value_part = parts[1].strip()
        
        first_quote = value_part.find('"')
        last_quote = value_part.rfind('"')
        
        if first_quote != -1 and last_quote != -1 and first_quote != last_quote:
            content = value_part[first_quote+1:last_quote]
            
            # Truncate logic: find the first 2 or 3 sentences
            # Split by . followed by space or end of string
            sentences = re.split(r'(?<=\.)\s+', content)
            short_content = " ".join(sentences[:2]) # Take first 2 sentences for safety (usually fits in 3 lines)
            
            # If still very long, truncate at 220 chars
            if len(short_content) > 220:
                short_content = short_content[:217] + "..."
            
            # Ensure it ends with a dot if it's not a truncation
            if not short_content.endswith('...') and not short_content.endswith('.'):
                short_content += '.'
                
            line = prefix + ' "' + short_content.replace('"', '\\"') + '",\n'
    new_lines.append(line)

with open(r'f:\conrutas\AppBeluso\src\data\pois.ts', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Truncated descriptions in pois.ts successfully")
