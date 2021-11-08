import os
import json
import curses
import requests
import random
def dl(url, filename):
	open(filename, 'wb').write(requests.get(url).content)
version = 34
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
def genpbar(percentage, showpercentage):
        if percentage > 100:
                return "error"
        pbarstr = "["
        pbar = percentage // 5
        for i in range(pbar):
                pbarstr += "#"
        for i in range(20 - pbar):
                pbarstr += " "
        pbarstr += "]"
        if showpercentage == True:
                pbarstr += str(percentage) + "%"
        return pbarstr
def nekodl(sfw, damount, stdscr):
        if damount == False:
                curses.echo()
                stdscr.attron(curses.color_pair(2))
                stdscr.addstr(8, 1, "Amount:")
                stdscr.attroff(curses.color_pair(2))
                amount = int(stdscr.getstr(8, 1 + len("Amount:")))
                stdscr.addstr(8, 1, "Amount:")
                curses.noecho()
        else:
                amount = amountd
                stdscr.addstr(8, 1, "Amount:" + str(amount))
        stdscr.addstr(11, 1, genpbar(0, True))
        stdscr.refresh()
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
                    stdscr.addstr(10, 1, "Duplicates: " + str(duplicates))
                    stdscr.addstr(11,1,genpbar(round((i+1)/amount*100), True))
                    stdscr.refresh()
                else:
                    urls.append(url)
                    dl(url, dir + getfilename(url))
                    stdscr.addstr(11,1,genpbar(round((i+1)/amount*100), True))
                    stdscr.refresh()
def urlsave(stdscr):
        with open('urlmap.json') as urlmap:
                url = json.load(urlmap)
        stdscr.addstr(8, 1, "Amount:" + str(len(url)))
        stdscr.addstr(11, 1, genpbar(0, True))
        stdscr.refresh()
        for i in range(len(url)):
                dl(url[i], dir + getfilename(url[i]))
                stdscr.addstr(11,1,genpbar(round((i+1)/len(url)*100), True))
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
name = "batchneko"
boxx = 78
boxy = 23
menu = ["[ sfw ]", "[ nsfw ]", "[ gif ]", "[ default ]", "[ urldump ]", "[ urlsave ]", "[ exit ]"]
Xs = [1]
topstr = "┌"
botstr = "└"
midstr = ""
linstr = ""
for i in range(boxx - len("[" + name + "]─┐")):
	topstr += "─"
	midstr += "─"
topstr += "[" + name + "]─┐"
for i in range(boxx - len("┘")):
	botstr += "─"
botstr += "┘"
for i in range(len(botstr) - 2):
	linstr += "─"
for i in range(len(menu)):
	Xs.append(len(menu[i]) + Xs[-1] + 2)
def display_menu(stdscr, sel_row, clear):
	if clear == True:
		stdscr.clear()
	stdscr.addstr(0, 0, topstr)
	stdscr.addstr(1, 1, "Welcome to " + name + "!")
	stdscr.addstr(2, 1, midstr)
	stdscr.addstr(3, 1, "version: " + str(version))
	stdscr.addstr(4, 1, "directory: " + dir)
	stdscr.addstr(5, 1, "default amount: " + str(amountd))
	stdscr.addstr(6, 1, "default arg: " + sfwd)
	stdscr.addstr(7, 1, midstr)
	stdscr.addstr(8, 1, "Amount:")
	stdscr.addstr(9, 1, "Duplicates:")
	stdscr.addstr(10, 1, midstr)
	stdscr.addstr(11, 1, genpbar(0, False))
	stdscr.addstr(boxy - 2, 1, linstr)
	stdscr.addstr(boxy, 0, botstr)
	for i in range(boxy - 1):
		stdscr.addstr(i+1, 0, "│")
		stdscr.addstr(i+1, boxx, "│")
	for idx, row in enumerate(menu):
		x = Xs[idx]
		y = boxy - 1
		if idx == sel_row:
			stdscr.attron(curses.color_pair(2))
			stdscr.addstr(y, x, row)
			stdscr.attroff(curses.color_pair(2))
		else:
			stdscr.addstr(y, x, row)
		stdscr.refresh()
def test(stdscr: 'curses._CursesWindow') -> int:
        global amount
        global zip
        global cmd
        h, w =stdscr.getmaxyx()
        try:
                curses.curs_set(0)
        except curses.error:
                pass
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_YELLOW)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_RED)
        current_row = 0
        display_menu(stdscr, current_row, False)
        while True:
                key = stdscr.getch()
                if key == curses.KEY_UP:
                        current_row = 0
                elif key == curses.KEY_DOWN:
                        current_row = len(menu) - 1
                elif key == curses.KEY_LEFT:
                        if current_row > 0:
                                current_row -= 1
                elif key == curses.KEY_RIGHT:
                        if current_row < len(menu) - 1:
                                current_row += 1
                elif key == curses.KEY_ENTER or key in [10, 13]:
                        if current_row == 0:
                                nekodl("s", False, stdscr)
                                stdscr.clear()
                        elif current_row == 1:
                                nekodl("n", False, stdscr)
                                stdscr.clear()
                        elif current_row == 2:
                                nekodl("g", False, stdscr)
                                stdscr.clear()
                        elif current_row == 3:
                                nekodl(sfwd, True, stdscr)
                                stdscr.clear()
                        elif current_row == 4:
                                cmd = "urldump"
                                break
                        elif current_row == 5:
                                urlsave(stdscr)
                                stdscr.clear()
                        elif current_row == 6:
                                exit()
                display_menu(stdscr, current_row, False)
while True:
        curses.wrapper(test)
        if cmd == "urldump":
                from tqdm import tqdm
                urldump()