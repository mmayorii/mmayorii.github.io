import os, json, random, requests
from tqdm import tqdm
def nekodl(sfw, amount):
        if sfw == "s":
            apiurl = ["https://nekos.life/api/v2/img/neko"]
        elif sfw == "n":
            apiurl=["https://nekos.life/api/v2/img/cum_jpg", "https://nekos.life/api/v2/img/lewd", "https://nekos.life/api/v2/img/pussy_jpg", "https://nekos.life/api/v2/img/lewdk", "https://nekos.life/api/v2/img/erokemo", "https://nekos.life/api/v2/img/blowjob", "https://nekos.life/api/v2/img/lewdkemo", "https://nekos.life/api/v2/img/tits", "https://nekos.life/api/v2/img/eroyuri", "https://nekos.life/api/v2/img/yuri", "https://nekos.life/api/v2/img/hentai"]
        elif sfw == "g":
            apiurl=["https://nekos.life/api/v2/img/feetg", "https://nekos.life/api/v2/img/cum", "https://nekos.life/api/v2/img/bj", "https://nekos.life/api/v2/img/spank", "https://nekos.life/api/v2/img/solog", "https://nekos.life/api/v2/img/Random_hentai_gif", "https://nekos.life/api/v2/img/pussy", "https://nekos.life/api/v2/img/pwankg", "https://nekos.life/api/v2/img/nsfw_neko_gif"]
        urls = []
        duplicates = 0
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
                    dl(url, dir + getfilename(url))
def dl(url, filename):
	open(filename, 'wb').write(requests.get(url).content)
def getfilename(url):
        if url.endswith("/"):
                purl = url[:-1]
        else:
                purl = url
        return purl.rsplit("/", 1)[1]
sfwd = "s"
amountd = 1
dir = ""
zip = False
if os.path.exists("config.json"):
        with open('config.json') as config:
                data = json.load(config)
                dir = data['savedir']
                askupdate = data['askupdate']
                sfwd = data['sfw']
                amountd = data['amount']
else:
        print("Created config file.")
        dir = input("Directory:")
        askupdate = "y"
        sfwd = input("Default nekodl argument: ")
        amountd = int(input("Default amount: "))
        writetojson = {'savedir':dir, 'askupdate':askupdate, 'amount':amountd, 'sfw':sfwd}
        with open('config.json', 'w') as c:
                json.dump(writetojson, c, indent=2)
while True:
        sfw = input("Nekodl >> ")
        if sfw == "help":
                print("List of commands:")
                print("help - print this menu")
                print("quit/exit - stop this script")
                print("update - update to main release")
                print("version - print the current version")
                print("empty command - use default settings")
                print("s/n/g - nekodl arguments")
        elif sfw == "quit" or sfw == "exit":
                exit()
        elif sfw == "update":
                dl("https://mmayorii.github.io/batchneko.py", "batchneko.py")
                os.remove("nekodl")
                exit()
        elif sfw == "version":
                print("Lite (21-M)")
        elif sfw == "":
                print("Using default settings")
                nekodl(sfwd, amountd)
        elif sfw == "s":
                nekodl("s", int(input("Amount:")))
        elif sfw == "n":
                nekodl("n", int(input("Amount:")))
        elif sfw == "g":
                nekodl("g", int(input("Amount:")))