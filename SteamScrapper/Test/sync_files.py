import json
import os

base = r'a:\Spring25\Big_Data\Scrapping\SteamScrapper\output'
cd = base + r'\Cleaned data'

# Build set of valid (app_id, recommendationid) from timestamps
valid_ts_keys = set()
with open(base + r'\reviews_timestamps_v3.json', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        data = json.loads(line)
        key = (str(data.get('app_id')), str(data.get('recommendationid')))
        valid_ts_keys.add(key)

# Filter reviews to only keep those with a matching timestamp
rev_path = cd + r'\reviews_data_cleaned.json'
temp_path = rev_path + '.tmp'
kept = 0
deleted = 0

with open(rev_path, 'r', encoding='utf-8') as f_in, open(temp_path, 'w', encoding='utf-8') as f_out:
    for line in f_in:
        line = line.strip()
        if not line:
            continue
        data = json.loads(line)
        key = (str(data.get('app_id')), str(data.get('recommendationid')))
        if key in valid_ts_keys:
            f_out.write(line + '\n')
            kept += 1
        else:
            deleted += 1

os.remove(rev_path)
os.rename(temp_path, rev_path)
print(f'Reviews kept: {kept}, deleted: {deleted}')

# Check if game 3265700 still has reviews
rev_ids = set()
with open(rev_path, 'r', encoding='utf-8') as f:
    for line in f:
        if line.strip():
            rev_ids.add(str(json.loads(line).get('app_id')))

has_game = '3265700' in rev_ids
print(f'Game 3265700 still has reviews: {has_game}')

# If game 3265700 has no reviews left, remove it from games, dlcs, and extra too
if not has_game:
    print('Removing game 3265700 from games and extra files...')
    for filepath, id_field in [
        (cd + r'\cleaned_games_data (1).json', 'app_id'),
        (cd + r'\cleaned_DLCS_data (1).json', 'parent_app_id'),
        (base + r'\games_extra_v3.json', 'app_id'),
    ]:
        tp = filepath + '.tmp'
        k = 0
        d = 0
        with open(filepath, 'r', encoding='utf-8') as fi, open(tp, 'w', encoding='utf-8') as fo:
            for line in fi:
                line = line.strip()
                if not line:
                    continue
                data = json.loads(line)
                if str(data.get(id_field)) != '3265700':
                    fo.write(line + '\n')
                    k += 1
                else:
                    d += 1
        os.remove(filepath)
        os.rename(tp, filepath)
        print(f'  {os.path.basename(filepath)}: kept {k}, removed {d}')
