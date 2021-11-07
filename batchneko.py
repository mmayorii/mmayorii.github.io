import os
import json
import curses
import requests
import random
def dl(url, filename):
	open(filename, 'wb').write(requests.get(url).content)
version = 29
sfwd = "s"
amountd = 1
dir = ""
zip = "n"
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
        if dir.endswith("/") == False:
                dir = dir + "/"
        askupdate = input("Check for updates automatically?(y/n)")
        sfwd = input("Default nekodl argument: ")
        amountd = int(input("Default amount: "))
        writetojson = {'savedir':dir, 'askupdate':askupdate, 'amount':amountd, 'sfw':sfwd}
        with open('config.json', 'w') as c:
                json.dump(writetojson, c, indent=2)
def Update():
        print("Checking for updates...")
        newver = int(requests.get("https://mmayorii.github.io/version.txt").content)
        if newver > version:
                print("New version available.")
                if input("Update? (y/n) ") == "y":
                        dl("https://mmayorii.github.io/batchneko.py", "update.py")
                        if os.path.exists("batchneko.py"):
                                os.remove("batchneko.py")
                        else:
                                print("Old batchneko script not found.")
                        os.rename("update.py", "batchneko.py")
                        print("Update installed.")
                        exit()
                else:
                        print("Not updating.")
        else:
                print("Your version is up to date.")
if askupdate == "y":
        Update()
def getfilename(url):
        if url.endswith("/"):
                purl = url[:-1]
        else:
                purl = url
        return purl.rsplit("/", 1)[1]
def nekodl(sfw, amount, stdscr):
        if sfw == "s":
            apiurl = ["https://nekos.life/api/v2/img/neko"]
        elif sfw == "n":
            apiurl=["https://nekos.life/api/v2/img/cum_jpg", "https://nekos.life/api/v2/img/lewd", "https://nekos.life/api/v2/img/pussy_jpg", "https://nekos.life/api/v2/img/lewdk", "https://nekos.life/api/v2/img/erokemo", "https://nekos.life/api/v2/img/blowjob", "https://nekos.life/api/v2/img/lewdkemo", "https://nekos.life/api/v2/img/tits", "https://nekos.life/api/v2/img/eroyuri", "https://nekos.life/api/v2/img/yuri", "https://nekos.life/api/v2/img/hentai"]
        elif sfw == "g":
            apiurl=["https://nekos.life/api/v2/img/feetg", "https://nekos.life/api/v2/img/cum", "https://nekos.life/api/v2/img/bj", "https://nekos.life/api/v2/img/spank", "https://nekos.life/api/v2/img/solog", "https://nekos.life/api/v2/img/Random_hentai_gif", "https://nekos.life/api/v2/img/pussy", "https://nekos.life/api/v2/img/pwankg", "https://nekos.life/api/v2/img/nsfw_neko_gif"]
        urls = []
        duplicates = 0
        for i in range(amount):
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
                    stdscr.addstr(0, 0, str(duplicates))
                else:
                    urls.append(url)
                    dl(url, dir + getfilename(url))
                    stdscr.addstr(h//2,w//2-3,str(round((i+1)/amount*100))+"%")
                    stdscr.refresh()
def urlsave(stdscr):
        with open('urlmap.json') as urlmap:
                url = json.load(urlmap)
        for i in range(len(url)):
                dl(url[i], getfilename(url[i]))
                stdscr.addstr(h//2,w//2-3,str(round((i+1)/len(url)*100))+"%")
                stdscr.refresh()
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
menu = ["sfw", "nsfw", "gif", "default", "urldump", "urlsave", "exit"]
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
        global amount
        global zip
        global cmd
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
                                curses.echo()
                                stdscr.attron(curses.color_pair(2))
                                stdscr.insstr(amy, amx, "Amount:")
                                stdscr.attroff(curses.color_pair(2))
                                amount = int(stdscr.getstr(amy, amx + len("Amount:")))
                                curses.noecho()
                                stdscr.clear()
                                stdscr.addstr(h//2,w//2-2,"0%")
                                stdscr.refresh()
                                nekodl("s", amount, stdscr)
                        elif current_row == 1:
                                curses.echo()
                                stdscr.attron(curses.color_pair(2))
                                stdscr.insstr(amy, amx, "Amount:")
                                stdscr.attroff(curses.color_pair(2))
                                amount = int(stdscr.getstr(amy, amx + len("Amount:")))
                                curses.noecho()
                                stdscr.clear()
                                stdscr.addstr(h//2,w//2-2,"0%")
                                stdscr.refresh()
                                nekodl("n", amount, stdscr)
                        elif current_row == 2:
                                curses.echo()
                                stdscr.attron(curses.color_pair(2))
                                stdscr.insstr(amy, amx, "Amount:")
                                stdscr.attroff(curses.color_pair(2))
                                amount = int(stdscr.getstr(amy, amx + len("Amount:")))
                                curses.noecho()
                                stdscr.clear()
                                stdscr.addstr(h//2,w//2-2,"0%")
                                stdscr.refresh()
                                nekodl("g", amount, stdscr)
                        elif current_row == 3:
                                stdscr.clear()
                                stdscr.addstr(h//2,w//2-2,"0%")
                                stdscr.refresh()
                                nekodl(sfwd, amountd, stdscr)
                        elif current_row == 4:
                                cmd = "urldump"
                                break
                        elif current_row == 5:
                                stdscr.clear()
                                stdscr.addstr(h//2,w//2-2,"0%")
                                stdscr.refresh()
                                urlsave(stdscr)
                        elif current_row == 6:
                                exit()
                display_menu(stdscr, current_row, False)
while True:
        curses.wrapper(test)
        if cmd == "urldump":
                from tqdm import tqdm
                urldump()