import requests
from bs4 import BeautifulSoup

r=requests.get("http://www.memecenter.com/top/daily")
soup=BeautifulSoup(r.content, "html.parser")
#print(soup.prettify())
#print(soup.find_all("a"))
"""
for i in soup.find_all("a"):
    print(i)
"""
for i in soup.find_all("a"):
    print(i.get("href"))
