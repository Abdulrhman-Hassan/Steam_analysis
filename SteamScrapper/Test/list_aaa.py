import json

filepath = r'a:\Spring25\Big_Data\Scrapping\SteamScrapper\output\Cleaned data\cleaned_games_data (1).json'
aaa_games = []

with open(filepath, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line.strip())
        if 'AAA_' in str(data.get('tag')):
            aaa_games.append(f"{data.get('name')} ({data.get('tag')})")

print(f'Found {len(aaa_games)} games with an AAA_ tag:')
for game in aaa_games:
    print(f'- {game}')
