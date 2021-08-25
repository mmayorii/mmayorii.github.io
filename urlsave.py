import os
from tqdm import tqdm
f = open("urlmap.txt")
url = f.readlines()
f.close()
for i in tqdm(range(len(url))):
    if url[i-1] != "Duplicate":
        os.system("curl --silent -O " + url[i-1])
