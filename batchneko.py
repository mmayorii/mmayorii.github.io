import os
import json
import sys
try:
	from tqdm import tqdm
except ModuleNotFoundError:
	os.system("python3 -m pip install tqdm > /dev/null 2>&1")
	from tqdm import tqdm
version = 18
sfwd = "s"
amountd = 1
dir = ""
zip = False
justupdated = False
args = sys.argv[1:]
if "--just-updated" in args:
        justupdated = True
        prever = int(args[1])
        if prever <= 16:
                print("Config is outdated.")
                os.system("rm config.json")
if os.path.exists("config.json"):
        with open('config.json') as config:
                data = json.load(config)
                asktozip = data['asktozip']
                dir = data['savedir']
                askupdate = data['askupdate']
                sfwd = data['sfw']
                amount = data['amount']
else:
        print("Created config file.")
        dir = input("Directory:")
        asktozip = input("Ask to zip at the end? (y/n)")
        askupdate = input("Check for updates automatically?(y/n)")
        sfwd = input("Default nekodl argument: ")
        amountd = int(input("Default amount: "))
        writetojson = {'savedir':dir,'asktozip':asktozip, 'askupdate':askupdate, 'amount':amountd, 'sfw':sfwd}
        with open('config.json', 'w') as c:
                json.dump(writetojson, c, indent=2)
def Update():
        print("Checking for updates...")
        os.system("curl -o version.txt https://mmayorii.github.io/version.txt --silent")
        f = open("version.txt", "r")
        if int(f.readline()) > version:
                print("New version available.")
                f.close()
                os.system("rm version.txt")
                if input("Update? (y/n):") == "y":
                        os.system("curl -o update.py https://mmayorii.github.io/batchneko.py --silent")
                        os.system("rm batchneko.py")
                        os.system("mv update.py batchneko.py")
                        print("Update installed.")
                        os.system("python3 batchneko.py --just-updated " + str(version))
                        exit()
                else:
                        print("Not updating.")
        else:
                print("Your version is up to date.")
                f.close()
                os.system("rm version.txt")
if justupdated == False:
        if askupdate != "n":
                Update()
if dir == "":
        print("Saving in current directory")
else:
        print("Saving in " + dir)
sfw = input("Args. (s/n/g/quit/advanced) ")
if sfw == "advanced":
        sfw = input("Advanced args. (reinstall/urldump/urlsave) ")
if sfw == "quit":
        exit()
elif sfw == "reinstall":
        print("Reinstalling script")
        os.system("curl -o install.py https://mmayorii.github.io/install.py --silent")
        os.system("python3 install.py")
        print("Done")
        exit()
elif sfw == "":
        print("Using default settings")
        sfw = sfwd
        amount = amountd
elif sfw == "urldump":
        if os.path.exists("urldump.py") == False:
                print("Downloading additional scripts...")
                os.system("curl --silent -O https://mmayorii.github.io/urldump.py")
                print("Done. Running script")
                os.system("python3 urldump.py")
                exit()
        os.system("python3 urldump.py")
        exit()
elif sfw == "urlsave":
        if os.path.exists("urlsave.py") == False:
                print("Downloading additional scripts...")
                os.system("curl --silent -O https://mmayorii.github.io/urlsave.py")
                print("Done. Running script")
                os.system("python3 urlsave.py")
                exit()
        os.system("python3 urlsave.py")
        exit()
else:
        amount = int(input("How many downloads? "))
if asktozip == "y":
        if input("Zip? (y/n)") == "y":
                zip = True
for i in tqdm(range(amount)):
        os.system("./nekodl -" + sfw)
print("Downloading done.")
if zip == True:
        os.system("zip -r nekos.zip ./nekos")
        os.system("rm -rf ./nekos")
        if dir != "":
                print("Moving files...")
                os.system("mv ./nekos.zip " + dir + "nekos.zip")
else:
        if dir != "":
                print("Moving files...")
                os.system("mv ./nekos " + dir + "nekos")
print("Done")
