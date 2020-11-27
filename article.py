import requests
from bs4 import BeautifulSoup

url = "https://humanparts.medium.com/aristotles-timeless-advice-on-what-real-friendship-is-and-why-it-matters-c0878418343f"
page = requests.get(url)
html = page.content.decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())

article = soup.find("article")
paragraphs = article.find_all("p")

for paragraph in paragraphs:
    print(paragraph.get_text())

# for x in paragraph_elements:
#
#     print(x.contents)
