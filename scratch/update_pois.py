import os
import json
import re

# Existing POIs from pois.ts (manually extracted or I'll read and parse)
# I'll read the file and use regex to find each POI block
with open(r'f:\conrutas\AppBeluso\src\data\pois.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Extracted data from source
with open(r'f:\conrutas\AppBeluso\scratch\extract_data.py', 'r') as f:
    # Wait, I didn't save the JSON to a file, I'll just hardcode the mapping here or run it again saving to file
    pass

# I'll just run the extraction script again and save to json
import subprocess
result = subprocess.run(['python', r'f:\conrutas\AppBeluso\scratch\extract_data.py'], capture_output=True, text=True)
source_data = json.loads(result.stdout)

# Mapping from source folder names to IDs in pois.ts
mapping = {
    "Area do Bon": "poi-area-bon",
    "Cabo Udra": "poi-cabo-udra",
    "Capilla Santos Reyes": "poi-capilla-reyes",
    "Humedal de Escorregadoiro": "poi-humedal",
    "Museo Masso": "poi-museo-masso",
    "Playa Banda do Rio": "poi-banda-rio",
    "Playa da Mourisca": "poi-mourisca",
    "Playa da Roiba": "poi-roiba",
    "Playa de Ancoradouro": "poi-ancoradouro",
    "Playa de Beluso": "poi-beluso-playa",
    "Playa de Pedrón": "poi-pedron",
    "Playa de Sartesens": "poi-sartesens",
    "Playa de Tuia": "poi-tulla",
    "Praia de Lagos": "poi-lagos",
    "Puerto Beluso": "poi-puerto-beluso",
    "Puerto de Bueu": "poi-lonja-bueu"
}

# Add coordinate for new POI
# 42.32694, -8.78889
source_data["Playa Banda do Rio"]["lat"] = 42.3270
source_data["Playa Banda do Rio"]["lng"] = -8.7891
source_data["Playa Banda do Rio"]["category"] = "playa"

# Function to clean description (remove google maps links and extra newlines)
def clean_desc(desc):
    desc = re.sub(r'https?://\S+', '', desc)
    desc = desc.strip().replace('\n', ' ')
    return desc

# I'll parse the pois.ts and update the relevant ones
# Using a simple list of POIs as objects
pois_json_str = re.search(r'export const DEFAULT_POIS: POI\[\] = \[(.*)\];', content, re.DOTALL).group(1)
# This is tricky to parse as JSON because it has comments and non-quoted keys sometimes
# But in this file it looks like a clean JSON-like structure except for comments

# I'll just do a series of replacements for each POI
new_content = content
for folder, id in mapping.items():
    if id == "poi-banda-rio": continue # Add separately
    
    data = source_data[folder]
    desc = clean_desc(data["description"])
    imgs = [f"/assets/pois/{folder}/{img}" for img in data["images"]]
    imgs_str = json.dumps(imgs, ensure_ascii=False)
    
    # Find the POI block by ID
    pattern = rf'(\{{\s*"id":\s*"{id}",.*?"description":\s*").*?(".*?"imgUrls":\s*)\[.*?\]'
    replacement = rf'\1{desc}\2{imgs_str}'
    new_content = re.sub(pattern, replacement, new_content, flags=re.DOTALL)

# Add Playa Banda do Rio before the cultura section
new_poi = f"""  {{
    "id": "poi-banda-rio",
    "lat": 42.3270,
    "lng": -8.7891,
    "name": "Playa Banda do Rio",
    "description": "{clean_desc(source_data["Playa Banda do Rio"]["description"])}",
    "category": "playa",
    "imgUrls": {json.dumps([f"/assets/pois/Playa Banda do Rio/{img}" for img in source_data["Playa Banda do Rio"]["images"]], ensure_ascii=False)}
  }},"""

if '"id": "poi-banda-rio"' not in new_content:
    new_content = new_content.replace('  //Punto Cultura//', new_poi + '\n\n  //Punto Cultura//')

with open(r'f:\conrutas\AppBeluso\src\data\pois.ts', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated pois.ts successfully")
