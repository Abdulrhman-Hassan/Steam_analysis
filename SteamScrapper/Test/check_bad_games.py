import json
import re

file_path = r'a:\Spring25\Big_Data\Scrapping\SteamScrapper\output\Cleaned data\cleaned_games_data (1).json'

patterns = {
    'Sexual/Nudity': re.compile(r'\b(nudity|sexual|nsfw|hentai|erotic|adult only|fan service|ecchi|loli|sexy)\b', re.IGNORECASE),
    'Gods/Polytheism': re.compile(r'\b(polytheism|pantheon|gods|deities|demigods)\b', re.IGNORECASE),
    'Gambling': re.compile(r'\b(gambling|casino|slot machine|slots|betting)\b', re.IGNORECASE)
}

found_games = []

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line: continue
            try:
                data = json.loads(line)
                name = data.get('name', '')
                
                # Combine text fields to search
                text_to_search = ' '.join(filter(None, [
                    data.get('name', ''),
                    data.get('description', ''),
                    data.get('short_description', ''),
                    data.get('genres', ''),
                    data.get('categories', '')
                ]))
                
                reasons = []
                for category, pattern in patterns.items():
                    matches = pattern.findall(text_to_search)
                    if matches:
                        unique_matches = set([m.lower() for m in matches])
                        reasons.append(f"{category} (matched: {', '.join(unique_matches)})")
                        
                if reasons:
                    found_games.append({'name': name, 'reasons': reasons})
            except json.JSONDecodeError:
                continue

    if found_games:
        print(f'Found {len(found_games)} potentially problematic games:')
        for g in found_games:
            print(f"- {g['name']}: {', '.join(g['reasons'])}")
    else:
        print('No games found matching those criteria.')
except Exception as e:
    print(f'Error: {e}')
