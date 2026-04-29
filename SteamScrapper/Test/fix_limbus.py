import json
import os

filepath = r'a:\Spring25\Big_Data\Scrapping\SteamScrapper\output\Cleaned data\cleaned_games_data (1).json'
temp_filepath = filepath + '.tmp'
fixed = False

with open(filepath, 'r', encoding='utf-8') as f_in, open(temp_filepath, 'w', encoding='utf-8') as f_out:
    for line in f_in:
        line = line.strip()
        if not line: continue
        
        data = json.loads(line)
        if str(data.get('app_id')) == '1973530':
            data['genres'] = 'RPG, Strategy'
            data['tag'] = 'AAA_RPG'
            data['tag_id'] = 122
            fixed = True
            
        f_out.write(json.dumps(data) + '\n')

if fixed:
    os.remove(filepath)
    os.rename(temp_filepath, filepath)
    print("Successfully fixed Limbus Company!")
else:
    os.remove(temp_filepath)
    print("Could not find Limbus Company.")
