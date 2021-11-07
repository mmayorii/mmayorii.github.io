import requests
type = input("Install normal or lite batchneko version? (n/l) ")
if type == "n":
  open("batchneko.py", "wb").write(requests.get("https://mmayorii.github.io/batchneko.py").content)
elif type == "l":
  open("batchneko.py", "wb").write(requests.get("https://mmayorii.github.io/batchneko-lite.py").content)
else:
  print("Input error.")
  exit()
print("Installed")
