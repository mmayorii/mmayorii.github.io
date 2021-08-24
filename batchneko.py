import os
import json
try:
	from tqdm import tqdm
except ModuleNotFoundError:
	os.system("python3 -m pip install tqdm > /dev/null 2>&1")
	from tqdm import tqdm
dir = ""
zip = False
if os.path.exists("reinstall"):
        os.system("rm reinstall")
        print("Reinstalling script")
        os.system("curl -o install.py https://mmayorii.github.io/install.py --silent")
        os.system("python3 install.py")
        print("Done")
        exit()
if os.path.exists("config.json"):
        with open('config.json') as config:
                data = json.load(config)
                asktozip = data['asktozip']
                dir = data['savedir']
else:
        print("Created config file.")
        dir = input("Directory:")
        asktozip = input("Ask to zip at the end? (y/n)")
        writetojson = {'savedir':dir,'asktozip':asktozip}
        with open('config.json', 'w') as c:
                json.dump(writetojson, c, indent=2)

print("Checking for updates...")
os.system("curl -o version.txt https://mmayorii.github.io/version.txt --silent")
f = open("version.txt", "r")
if int(f.read()) > 7:
        print("New version available.")
        if input("Update? (y/n):") == "y":
                f.close()
                os.system("rm version.txt")
                os.system("curl -o update.py https://mmayorii.github.io/batchneko.py --silent")
                os.system("rm batchneko.py")
                os.system("mv update.py batchneko.py")
                print("Update installed.")
                os.system("python3 batchneko.py")
                exit()
        else:
                print("Not updating.")
else:
        print("Your version is up to date.")
        f.close()
        os.system("rm version.txt")
if dir == "":
        print("Saving in current directory")
sfw = input("SFW or NSFW? (s/n/g) ")
amount = int(input("How many downloads? "))
if asktozip == "y":
        if input("Zip? (y/n)") == "y":
                zip = True
for i in tqdm(range(amount)):
        os.system("./nekodl -" + sfw)
if dir != "":
        if zip == True:
                os.system("zip -r nekos.zip ./nekos")
                os.system("rm -rf ./nekos")
                os.system("mv ./nekos.zip " + dir + "nekos.zip")
        else:
                os.system("mv ./nekos " + dir + "nekos")
print("Done")
