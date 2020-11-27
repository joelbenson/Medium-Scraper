import requests
import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup


class User:

    def __init__(self, url):
        self.parsed_url = urlparse(url)
        self.page_soup = BeautifulSoup(requests.get(url).content.decode('utf-8'), 'html.parser')
        try:
            self.username = re.findall(r'@[0-9a-zA-Z._]+', self.parsed_url.geturl())[0]
        except:
            self.username = '@' + re.findall(r'[0-9a-zA-Z_]+', self.parsed_url.netloc)[0]

        self.name = self.page_soup.find("a", attrs={"aria-label":"Author Homepage"}).get_text()
        if (not self.name):
            self.name = self.page_soup.find("a", {"aria-label":"Author Homepage"}).find('img')['alt']

    def get_articles(self):
        articles = []
        for article in self.page_soup.find_all('h1'):
            articles.append(Article(article.find('a')['href']))
        return articles


class Article:

    def __init__(self, url):
        self.parsed_url = urlparse(url)
        self.page_soup = BeautifulSoup(requests.get(url).content.decode('utf-8'), 'html.parser')
        self.title = self.page_soup.find('h1').get_text()

    def get_paragraphs(self):
        content = self.page_soup.find_all('p')
        paragraphs = []
        for paragraph in content:
            paragraphs.append(paragraph.get_text())

    def get_user(self):
        user_element = self.page_soup.select('a > h4')
        user_parsed_url = urlparse(user_element[0].parent['href'])

        if (user_parsed_url.netloc):
            user = User(user_parsed_url.geturl())
        else:
            user = User("https://" + self.parsed_url.netloc + user_parsed_url.geturl())
        return user

    def get_publication(self):
        publication_parsed_url = urlparse(self.page_soup.select('a > div > img')[0].parent.parent['href'])
        if (publication_parsed_url.netloc):
            publication = Publication(publication_parsed_url.geturl())
        else:
            publication = Publication("https://" + self.parsed_url.netloc + publication_parsed_url.geturl())

        return publication

    def get_tags(self):
        for tag in self.page_soup.find_all('a', href=re.compile('/tagged/')):
            tag_url = tag['href']
            tag_url_parsed = urlparse(tag['href'])
            if (not tag_url_parsed.netloc):
                tag_url = "https://" + self.parsed_url.netloc + tag_url
            self.tags.append(Tag(tag_url, tag.get_text()))


class Publication:
    
    def __init__(self, url):
        self.parsed_url = urlparse(url)
        self.id = None
        self.name = None
        self.description = None
        self.url = url
        self.imageUrl = None
        self.users = None
        self.articles = None

    def get_users(self):
        return

    def get_articles(self):
        return

class Tag:
    def __init__(self, url, name):
        self.parsed_url = urlparse(url)
        self.name = name
