import os
os.system("curl -o update.py https://mmayorii.github.io/batchneko-lite.py")
os.system("curl -o update https://mmayorii.github.io/nekodl")
os.system("rm batchneko.py")
os.system("mv update.py batchneko.py")
os.system("rm nekodl")
os.system("mv update nekodl")
os.system("chmod +x nekodl")
os.system("rm install.py")
