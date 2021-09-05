import os, json
from tqdm import tqdm
sfwd = "s"
amountd = 1
dir = ""
zip = False
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
        askupdate = "y"
        sfwd = input("Default nekodl argument: ")
        amountd = int(input("Default amount: "))
        writetojson = {'savedir':dir,'asktozip':asktozip, 'askupdate':askupdate, 'amount':amountd, 'sfw':sfwd}
        with open('config.json', 'w') as c:
                json.dump(writetojson, c, indent=2)
while True:
        default = False
        invalid = False
        sfw = input("Nekodl >> ")
        if sfw == "help":
                print("List of commands:")
                print("help - print this menu")
                print("quit/exit - stop this script")
                print("update - update to main release")
                print("version - print the current version")
                print("empty command - use default settings")
                print("urldump - create a urlmap")
                print("urlsave - use a urlmap to save files from it")
                print("s/n/g - nekodl arguments")
        elif sfw == "quit" or sfw == "exit":
                exit()
                print("Exiting.")
        elif sfw == "update":
                print("Updating to main release")
                os.system("curl -o install.py https://mmayorii.github.io/install.py --silent")
                os.system("python3 install.py")
                os.system("python3 batchneko.py")
                exit()
        elif sfw == "version":
                print("Lite (21-M)")
        elif sfw == "":
                print("Using default settings")
                sfw = sfwd
                amount = amountd
                default = True
        elif sfw == "urldump":
                if os.path.exists("urldump.py") == False:
                        print("Downloading additional scripts...")
                        os.system("curl --silent -O https://mmayorii.github.io/urldump.py")
                os.system("python3 urldump.py")
        elif sfw == "urlsave":
                if os.path.exists("urlsave.py") == False:
                        print("Downloading additional scripts...")
                        os.system("curl --silent -O https://mmayorii.github.io/urlsave.py")
                os.system("python3 urlsave.py")
        else:
                invalid = True
        if sfw == "s" or sfw == "n" or sfw == "g":
                if default == False:
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
        elif invalid == True:
                print("Invalid command. Run help to see list of commands.")
