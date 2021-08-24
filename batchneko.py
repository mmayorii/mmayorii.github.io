import os
try:
	from tqdm import tqdm
except ModuleNotFoundError:
	os.system("python3 -m pip install tqdm > /dev/null 2>&1")
	from tqdm import tqdm
dir = input("Directory:")
sfw = input("SFW or NSFW? (s/n/g) ")
amount = int(input("How many downloads? "))
if input("Zip? (y/n)") == "y":
	zip = True
for i in tqdm(range(amount)):
	os.system("./nekodl -" + sfw)
if zip == True:
	os.system("zip -r nekos.zip ./nekos")
	os.system("rm -rf ./nekos")
	os.system("mv ./nekos.zip " + dir + "nekos.zip")
else:
	os.system("mv ./nekos " + dir + "nekos")
print("Done")