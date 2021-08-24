import os
try:
	from tqdm import tqdm
except ModuleNotFoundError:
	os.system("python3 -m pip install tqdm > /dev/null 2>&1")
	from tqdm import tqdm
old = False
dir = ""
if os.path.exists("config.txt"):
        c = open("config.txt", "r")
        dir = c.read()
        c.close()
else:
        c = open("config.txt", "w")
        print("Created config file.")
        dir = input("Directory:")
        c.write(dir)
        c.close()

print("Checking for updates...")
os.system("curl -o version.txt https://mmayorii.github.io/version.txt --silent")
f = open("version.txt", "r")
if int(f.read()) > 3:
        print("New version available. Updating...")
        f.close()
        os.system("rm version.txt")
        os.system("curl -o update.py https://mmayorii.github.io/batchneko.py --silent")
        os.system("rm batchneko.py")
        os.system("mv update.py batchneko.py")
        old = True
        print("Update installed.")
        os.system("python3 batchneko.py")
else:
        print("Your version is up to date.")
        f.close()
        os.system("rm version.txt")
if old == False:
        if dir == "":
                print("Saving in current directory")
        sfw = input("SFW or NSFW? (s/n/g) ")
        amount = int(input("How many downloads? "))
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
