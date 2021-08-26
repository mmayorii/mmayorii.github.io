import json, random, os
from tqdm import tqdm
import requests
apiurl = ["https://nekos.life/api/v2/img/neko"]
duplicates = 0
urls = []
amount = int(input("Amount:"))
for i in tqdm(range(amount)):
    randapiurl = random.choice(apiurl)
    try:
        randapicontent = requests.get(randapiurl)
    except Exception:
        randapiurl = random.choice(apiurl)
    data = json.loads(randapicontent.content)
    url = data['url']
    if url.find('/'):
        if url in urls:
            duplicates += 1
        else:
            urls.append(url)
        i += 1
with open('urlmap.json', 'w') as urlmap:
    json.dump(urls, urlmap, indent=2)
print(duplicates)