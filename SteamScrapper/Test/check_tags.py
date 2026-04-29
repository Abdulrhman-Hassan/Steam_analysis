import json

filepath = r'a:\Spring25\Big_Data\Scrapping\SteamScrapper\output\Cleaned data\cleaned_games_data (1).json'

normal_tags = set()
rescrape_count = 0

with open(filepath, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line.strip())
        t = data.get('tag')
        if t == 'Rescrape':
            rescrape_count += 1
        elif t:
            normal_tags.add(t)

print(f'Rescrape count: {rescrape_count}')
print(f'Normal tags found (sample): {list(normal_tags)[:10]}')

