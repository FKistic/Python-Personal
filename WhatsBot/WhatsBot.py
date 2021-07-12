import time,os
from bs4 import BeautifulSoup
import requests
url='https://web.whatsapp.com/'
r=requests.get(url)
html_content=r.content
soup=BeautifulSoup(html_content,'html.parser')
print(soup)