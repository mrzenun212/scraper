import requests
import os.path
import json
from bs4 import BeautifulSoup

url = "https://yts.ag/"


r = requests.get(url)
soup = BeautifulSoup(r.content)
data = soup.find_all("a", {"class": "browse-movie-title"})
count = 0

def scrape(data):
	for item in data:
		print item.text
	

scrape(data)

