import json
import os

filepath = r'a:\Spring25\Big_Data\Scrapping\SteamScrapper\output\Cleaned data\cleaned_games_data (1).json'
temp_filepath = filepath + '.tmp'

updated_count = 0

with open(filepath, 'r', encoding='utf-8') as f_in, open(temp_filepath, 'w', encoding='utf-8') as f_out:
    for line in f_in:
        line = line.strip()
        if not line:
            continue
        
        try:
            data = json.loads(line)
            # Rename 'categories' to 'features'
            if 'categories' in data:
                data['features'] = data.pop('categories')
                updated_count += 1
                
            f_out.write(json.dumps(data) + '\n')
        except Exception as e:
            print(f'Error on line: {e}')
            
os.remove(filepath)
os.rename(temp_filepath, filepath)

print(f'Successfully renamed categories to features in {updated_count} games.')
