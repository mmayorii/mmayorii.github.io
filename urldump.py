import json, random, os
from tqdm import tqdm
import requests
apiurl = ["https://nekos.life/api/v2/img/neko"]
def log(logtext):
    l = open("urlmap.txt", 'a')
    l.write(logtext)
    l.write('\n')
    l.close()
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
            urls.append("Duplicate")
        else:
            urls.append(url)
        i += 1
        fi = i
for i in tqdm(range(fi)):
    log(urls[i])
print(duplicates)