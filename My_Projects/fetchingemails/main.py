import requests
from bs4 import BeautifulSoup
import re
def get_emails(industry):
    # Set the URL of the search page
    url = "https://www.google.com/search?q=site:linkedin.com+intext:'AEC+industry'+intext:'email'"

    # Set the user agent to mimic a real browser
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    # Send the request and get the response
    response = requests.get(url, headers=headers)

    # Parse the response with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the email addresses on the page

    emails = soup.find_all(text=re.compile('[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,4}'))

    # Print the emails
    for email in emails:
        print(email)

# Fetch the emails for the AEC industry
get_emails("BIM modelling")