import MediumUtils as M


TOPICS = ['philosophy', 'sleep']
REQUEST_WAIT_TIME = 1


def main():

    # publications = M.publicationsFromTopics(TOPICS, REQUEST_WAIT_TIME)

    # users = M.usersFromTopics(TOPICS, REQUEST_WAIT_TIME)

    articles = M.articlesFromTopics(TOPICS)

    M.printArticles(articles)



if __name__ == "__main__":
    main()
