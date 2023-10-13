from selenium import webdriver
from bs4 import BeautifulSoup
import requests

chrome_driver_path = "./chromedriver.exe"

date = input("Which year would you like to travel? format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
# code = response.status_code
# print(code)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())
song_spans = soup.findAll("h3", class_="a-no-trucate")
songs = []
for song in song_spans:
    text = song.text
    text = text.replace("\n", "")
    songs.append(text)
print(songs)
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver.get("https://www.amazon.com")
