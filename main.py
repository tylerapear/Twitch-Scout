import requests
from bs4 import BeautifulSoup

response = requests.get('https://google.com')

html_doc = response.text

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())