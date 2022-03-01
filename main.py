import bs4
from bs4 import BeautifulSoup
import requests 

url = "https://www.hinatazaka46.com/s/official/search/artist"
r = requests.get(url)
s = BeautifulSoup(r.text, 'html')
print(s.prettify())
