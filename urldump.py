def urldump():
        urls = []
        if input("Import a urlmap (urlmapold.json)? (y/n) ") == "y":
            with open('urlmapold.json') as urlmapold:
                urls = json.load(urlmapold)
        sfw = input("Image type (s/n/g) ")
        if sfw == "s":
            apiurl = ["https://nekos.life/api/v2/img/neko"]
        elif sfw == "n":
            apiurl=["https://nekos.life/api/v2/img/cum_jpg", "https://nekos.life/api/v2/img/lewd", "https://nekos.life/api/v2/img/pussy_jpg", "https://nekos.life/api/v2/img/lewdk", "https://nekos.life/api/v2/img/erokemo", "https://nekos.life/api/v2/img/blowjob", "https://nekos.life/api/v2/img/lewdkemo", "https://nekos.life/api/v2/img/tits", "https://nekos.life/api/v2/img/eroyuri", "https://nekos.life/api/v2/img/yuri", "https://nekos.life/api/v2/img/hentai"]
        elif sfw == "g":
            apiurl=["https://nekos.life/api/v2/img/feetg", "https://nekos.life/api/v2/img/cum", "https://nekos.life/api/v2/img/bj", "https://nekos.life/api/v2/img/spank", "https://nekos.life/api/v2/img/solog", "https://nekos.life/api/v2/img/Random_hentai_gif", "https://nekos.life/api/v2/img/pussy", "https://nekos.life/api/v2/img/pwankg", "https://nekos.life/api/v2/img/nsfw_neko_gif"]
        else:
            print("Input error. Using sfw")
            apiurl = ["https://nekos.life/api/v2/img/neko"]
        duplicates = 0
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
from tqdm import tqdm
import random, json, requests
urldump()