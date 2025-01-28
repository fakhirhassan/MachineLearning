# https://python.langchain.com/docs/introduction/
# https://python.langchain.com/docs/concepts/
# https://python.langchain.com/docs/tutorials/

import threading
import time
from bs4 import BeautifulSoup
import requests

url = [
    'https://python.langchain.com/docs/introduction/',
    'https://python.langchain.com/docs/concepts/',
    'https://python.langchain.com/docs/tutorials/'
]
def getHtml(url): 
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(len(soup.text))

thread = []

for urls in url:
    t = threading.Thread(target=getHtml, args=(urls,))
    t.start()
    thread.append(t)
for th in thread:
    th.join()
