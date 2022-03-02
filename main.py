import bs4
from bs4 import BeautifulSoup
import requests 
import csv 

url = "https://www.hinatazaka46.com/s/official/search/artist"
r = requests.get(url)
s = BeautifulSoup(r.text, 'lxml')
# print(s.prettify())
members_list = ''
for i in range(1, 8):
  name_selector = f'body > div.l-wrap.p-wrap__bg > main > section > div > div.sorted.sort-default.current > div:nth-child(2) > div > ul > li:nth-child({i}) > a > div.c-member__name'
  members = s.select(name_selector)
  members_html = members[0]
  members_text = members_html.text.split()
  members_name = ''.join(members_text)
  members_list += members_name + "\n"


with open('data/output/text/member.txt', 'w') as f:
  f.write(members_list)
