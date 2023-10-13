from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.moneycontrol.com/")
page = response.text

soup = BeautifulSoup(page, "html.parser")

tag = soup.select_one(selector="tbody tr td a")
print(tag)