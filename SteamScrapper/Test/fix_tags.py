import json
import os

filepath = r'a:\Spring25\Big_Data\Scrapping\SteamScrapper\output\Cleaned data\cleaned_games_data (1).json'
temp_filepath = filepath + '.tmp'

# Known mappings from the spider
GENRE_MAP = {
    "Action": 19,
    "Adventure": 21,
    "RPG": 122,
    "Strategy": 9,
    "Simulation": 599,
    "Horror": 1667,
    "Puzzle": 1664,
    "Platformer": 1625,
    "Survival": 1662,
    "FPS": 1663,
    "Open World": 1695,
    "Casual": 597
}

updated_count = 0

with open(filepath, 'r', encoding='utf-8') as f_in, open(temp_filepath, 'w', encoding='utf-8') as f_out:
    for line in f_in:
        line = line.strip()
        if not line: continue
        
        data = json.loads(line)
        
        if data.get('tag') == 'Rescrape':
            genres_raw = data.get('genres', '')
            genres_list = [g.strip() for g in genres_raw.split(',')]
            
            # Determine prefix
            is_indie = 'Indie' in genres_list
            prefix = "Indie" if is_indie else "AAA"
            
            # Find the best matching genre from our map
            matched_genre = None
            matched_id = 0
            for g in genres_list:
                if g in GENRE_MAP:
                    matched_genre = g
                    matched_id = GENRE_MAP[g]
                    break
            
            if matched_genre:
                new_tag = f"{prefix}_{matched_genre}"
                new_id = matched_id
            else:
                # Fallback if none of the specific tags match
                fallback = genres_list[0] if genres_list else "Unknown"
                new_tag = f"{prefix}_{fallback}"
                new_id = 0
                
            data['tag'] = new_tag
            data['tag_id'] = new_id
            updated_count += 1
            
        f_out.write(json.dumps(data) + '\n')

os.remove(filepath)
os.rename(temp_filepath, filepath)

print(f'Successfully fixed the tag and tag_id for {updated_count} rescraped games.')
