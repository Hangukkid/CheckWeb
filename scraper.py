import time
import requests 
from bs4 import BeautifulSoup 
import webbrowser

url = "https://instockps5.ca/"

og = requests.get(url, timeout=10)
og = BeautifulSoup(og.content, 'html5lib')
while (1):
    time.sleep(10)
    new_update = requests.get(url, timeout=10)
    new_update = BeautifulSoup(new_update.content, 'html5lib')
    if (og != new_update):
        webbrowser.open(url)
        og = new_update
