from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/"

response = requests.get(url)

page = response.text

soup = BeautifulSoup(page, "html.parser")
article_titles = []
article_links = []
article_tags = soup.find_all(name="a", class_="titlelink")

for article_tag in article_tags:
    title = article_tag.get_text()
    link = article_tag.get("href")
    article_titles.append(title)
    article_links.append(link)

article_upvote = [upvote.get_text() for upvote in soup.find_all(name="span", class_="score")]

print(article_links)
print(article_titles)
points = []
largest = []
for upvote in article_upvote:
    upvote = upvote.replace(" points", "")
    points.append(int(upvote))
    largest.append(int(upvote))

largest.sort()

i = points.index(max(points))
print(max(points))
print(article_links[i])
print(article_titles[i])