import os, json
from tqdm import tqdm
with open('urlmap.json') as urlmap:
    url = json.load(urlmap)
for i in tqdm(range(len(url))):
    os.system("curl --silent -O " + url[i-1])
