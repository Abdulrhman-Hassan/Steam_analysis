import json

filepath = r'a:\Spring25\Big_Data\Scrapping\SteamScrapper\output\Cleaned data\cleaned_games_data (1).json'
extrapath = r'a:\Spring25\Big_Data\Scrapping\SteamScrapper\output\games_extra_v3.json'

games_to_find = {'1295920', '427520'}
prices = {}

with open(filepath, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line.strip())
        app_id = str(data.get('app_id'))
        if app_id in games_to_find:
            prices[app_id] = data.get('price')

print(f"Prices from main file: {prices}")

# Update the extra file
temp_extra = extrapath + '.tmp'
updated = 0

with open(extrapath, 'r', encoding='utf-8') as f_in, open(temp_extra, 'w', encoding='utf-8') as f_out:
    for line in f_in:
        data = json.loads(line.strip())
        app_id = str(data.get('app_id'))
        
        if app_id in prices:
            # Format the numeric price from main file into the $0.00 string format used in original_price
            numeric_price = prices[app_id]
            formatted_price = f"${numeric_price:.2f}" if numeric_price is not None else None
            data['original_price'] = formatted_price
            updated += 1
            
        f_out.write(json.dumps(data) + '\n')

import os
os.remove(extrapath)
os.rename(temp_extra, extrapath)

print(f"Updated {updated} prices.")
