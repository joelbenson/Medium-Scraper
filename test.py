from models import User, Article

# Joel = User('https://medium.com/@jcbenson/')
# Katie = User('https://mgsiegler.medium.com/')
article = Article("https://psiloveyou.xyz/5-attractive-traits-that-dont-actually-make-him-a-good-long-term-partner-3c907567b177")

# print(Joel.articles)
# print(Katie.articles[0].url)
print(article.get_publication().parsed_url.geturl())
