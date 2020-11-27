import requests
from bs4 import BeautifulSoup
import time

def publicationsFromTopics(topics, requestWaitTime=1):
    #input: [(str) topic]
    #output: [{(str)url, (str)title} publication]

    publications = []

    #for each topic, find names of publications lists when topic is searched on Medium
    for topic in topics:

        url = "https://medium.com/search/publications?q={}".format(topic)
        time.sleep(requestWaitTime)
        page = requests.get(url)
        html = page.content.decode('utf-8')

        soup = BeautifulSoup(html, 'html.parser')
        publication_elements = soup.find_all("a", attrs={"rel":"collection"})

        for publication_element in publication_elements:
            publication = {
                "title": publication_element.contents[0],
                "url": publication_element['href']
            }

            publications.append(publication)

    #reduce list to unique values
    publications = list({v['url']:v for v in publications}.values())

    return publications

def usersFromTopics(topics, requestWaitTime=1):
    #input: [(str) topic]
    #output: [{(str)url, (str)name} user]

    users = []

    #for each topic, find names of publications lists when topic is searched on Medium
    for topic in topics:

        url = "https://medium.com/search/users?q={}".format(topic)
        time.sleep(requestWaitTime)
        page = requests.get(url)
        html = page.content.decode('utf-8')

        soup = BeautifulSoup(html, 'html.parser')
        user_elements = soup.find_all("a", attrs={"rel":"author"})

        for user_element in user_elements:
            user = {
                "name": user_element.contents[0],
                "url": user_element['href']
            }

            users.append(user)

    #reduce list to unique values
    users = list({v['url']:v for v in users}.values())

    return users

def articlesFromTopics(topics, requestWaitTime=1):

    articles = []

    #for each topic, find names of publications lists when topic is searched on Medium
    for topic in topics:

        url = "https://medium.com/search?q={}".format(topic)
        time.sleep(requestWaitTime)
        page = requests.get(url)
        html = page.content.decode('utf-8')

        soup = BeautifulSoup(html, 'html.parser')
        article_elements = soup.find_all("a", attrs={"data-action":"open-post"})

        for article_element in article_elements:

            article = {
                "url": article_element['href'],
            }

            articles.append(article)

    #reduce list to unique values
    articles = list({v['url']:v for v in articles}.values())

    return articles


def printPublications(publications):
    #input: [{(str)url, (str)title} publication]
    #output: None

    print('----------')

    for publication in publications:
        print(publication['title'])
        print("({})".format(publication['url']))
        print('----------')

def printUsers(users):
    #input: [{(str)url, (str)name} user]
    #output: None

    print('----------')

    for user in users:
        print(user['name'])
        print("({})".format(user['url']))
        print('----------')

def printArticles(articles):

    print('----------')

    for article in articles:
        print(article['url'])
        print('----------')
