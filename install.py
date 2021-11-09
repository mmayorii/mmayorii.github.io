import requests
type = input("Install normal or lite batchneko version? (n/l) ")
if type == "n":
  open("batchneko.py", "wb").write(requests.get("https://phil213314.github.io/batchneko/batchneko.py").content)
elif type == "l":
  open("batchneko.py", "wb").write(requests.get("https://phil213314.github.io/batchneko/batchneko-lite.py").content)
else:
  print("Input error.")
  exit()
print("Installed")
