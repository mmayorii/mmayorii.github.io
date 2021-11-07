import requests
open("batchneko.py", "wb").write(requests.get("https://mmayorii.github.io/batchneko.py").content)
print("Installed")