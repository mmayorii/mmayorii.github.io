import os
import json
import sys
import curses
import requests
import random
try:
	from tqdm import tqdm
except ModuleNotFoundError:
	os.system("python3 -m pip install tqdm > /dev/null 2>&1")
	from tqdm import tqdm
version = 24
sfwd = "s"
amountd = 1
dir = ""
zip = "n"
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
                zip = data['asktozip']
                dir = data['savedir']
                askupdate = data['askupdate']
                sfwd = data['sfw']
                amountd = data['amount']
else:
        print("Created config file.")
        dir = input("Directory:")
        asktozip = input("Zip downloaded files? (y/n)")
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
def urldump():
        urls = []
        if input("Import a urlmap? (y/n) ") == "y":
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
def urlsave():
        with open('urlmap.json') as urlmap:
            url = json.load(urlmap)
        for i in tqdm(range(len(url))):
            os.system("curl --silent -O " + url[i-1])
menu = ["sfw", "nsfw", "gif", "default", "urldump", "urlsave", "reinstall", "exit"]
col = 1
amx = 0
amy = 0
def display_menu(stdscr, sel_row, clear):
        global col
        global h
        global w
        global amx
        global amy
        if clear == True:
                stdscr.clear()
        amx = w//2 - len("Amount:")//2
        amy = h//2 - len(menu)//2 - 1
        for idx, row in enumerate(menu):
                x = w//2 - len(row)//2
                y = h//2 - len(menu)//2 + idx
                if idx == sel_row:
                        stdscr.attron(curses.color_pair(col))
                        stdscr.addstr(y, x, row)
                        stdscr.attroff(curses.color_pair(col))
                else:
                        stdscr.addstr(y, x, row)
                stdscr.refresh()


def test(stdscr: 'curses._CursesWindow') -> int:
        global col
        global h
        global w
        global sfw
        global amount
        global zip
        h, w =stdscr.getmaxyx()
        try:
                curses.curs_set(0)
        except curses.error:
                stdscr.attron(curses.color_pair(1))
                stdscr.insstr(0, 0, "Your terminal does not support cursor hiding. You may experience issues")
                stdscr.attroff(curses.color_pair(1))
        stdscr.addstr(h - 1, 0, "version: " + str(version))
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_YELLOW)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_RED)
        current_row = 0
        display_menu(stdscr, current_row, False)
        while True:
                key = stdscr.getch()
                if key == curses.KEY_UP:
                        if current_row > 0:
                                current_row -= 1
                elif key == curses.KEY_DOWN:
                        if current_row < len(menu) - 1:
                                current_row += 1
                elif key == curses.KEY_LEFT:
                        current_row = 0
                elif key == curses.KEY_RIGHT:
                        current_row = len(menu) - 1
                elif key == curses.KEY_ENTER or key in [10, 13]:
                        if current_row == 0:
                                sfw = "s"
                                curses.echo()
                                stdscr.attron(curses.color_pair(2))
                                stdscr.insstr(amy, amx, "Amount:")
                                stdscr.attroff(curses.color_pair(2))
                                amount = int(stdscr.getstr(amy, amx + len("Amount:")))
                                curses.noecho()
                                stdscr.clear()
                                break
                        elif current_row == 1:
                                sfw = "n"
                                curses.echo()
                                stdscr.attron(curses.color_pair(2))
                                stdscr.insstr(amy, amx, "Amount:")
                                stdscr.attroff(curses.color_pair(2))
                                amount = int(stdscr.getstr(amy, amx + len("Amount:")))
                                curses.noecho()
                                stdscr.clear()
                                break
                        elif current_row == 2:
                                sfw = "g"
                                curses.echo()
                                stdscr.attron(curses.color_pair(2))
                                stdscr.insstr(amy, amx, "Amount:")
                                stdscr.attroff(curses.color_pair(2))
                                amount = int(stdscr.getstr(amy, amx + len("Amount:")))
                                curses.noecho()
                                stdscr.clear()
                                break
                        elif current_row == 3:
                                sfw = ""
                                break
                        elif current_row == 4:
                                sfw = "urldump"
                                break
                        elif current_row == 5:
                                sfw = "urlsave"
                                break
                        elif current_row == 6:
                                sfw = "reinstall"
                                break
                        elif current_row == 7:
                                sfw = "quit"
                                break
                display_menu(stdscr, current_row, False)
while True:
        curses.wrapper(test)
        if sfw == "quit":
                exit()
        elif sfw == "reinstall":
                os.system("curl -o install.py https://mmayorii.github.io/install.py --silent")
                os.system("python3 install.py")
                os.system("python3 batchneko.py")
                exit()
        elif sfw == "":
                sfw = sfwd
                amount = amountd
        elif sfw == "urldump":
                urldump()
        elif sfw == "urlsave":
                urlsave()
        if sfw == "s" or sfw == "n" or sfw == "g":
                for i in tqdm(range(amount)):
                        os.system("./nekodl -" + sfw)
                if zip == "y":
                        os.system("zip -r nekos.zip ./nekos")
                        os.system("rm -rf ./nekos")
                        if dir != "":
                                os.system("mv ./nekos.zip " + dir + "nekos.zip")
                else:
                        if dir != "":
                                os.system("mv ./nekos " + dir + "nekos")
