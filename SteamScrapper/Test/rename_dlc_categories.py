import json
import os

filepath = r'a:\Spring25\Big_Data\Scrapping\SteamScrapper\output\Cleaned data\cleaned_DLCS_data (1).json'
temp_filepath = filepath + '.tmp'
updated = 0

with open(filepath, 'r', encoding='utf-8') as f_in, open(temp_filepath, 'w', encoding='utf-8') as f_out:
    for line in f_in:
        line = line.strip()
        if not line: continue
        
        data = json.loads(line)
        
        if 'categories' in data:
            data['features'] = data.pop('categories')
            updated += 1
            
        f_out.write(json.dumps(data) + '\n')

os.remove(filepath)
os.rename(temp_filepath, filepath)

print(f"Successfully renamed 'categories' to 'features' for {updated} DLC records.")
