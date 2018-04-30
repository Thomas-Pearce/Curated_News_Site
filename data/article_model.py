from data import DBClient
import datetime

""""Articles have the following format in the DB

{'_id': "MongoDB id as a mongo objectID object", 
'docid': 'Lexxes internal document ID as a string', 
'date': 'The date of scrape as a string', 
'time': 'The time of scrape as a string', 
'istopnews': "A boolean stating whether the article was at the top of the page", 
'source': 'The name of the publisher as a string', 
'url': 'The url of the article as a string', 
'title': 'The title of the article as a string.', 
'content': 'The content of the article as a string', 
'sindices': "Lexxes sentiment analysis in the format of a list of dicts with the format name score", 
'datetime': "The datetime of the scrape as a python datetime object"}
"""


def get_breaking(count = 6):
    """"Returns the breaking news as a list of dicts.

    For now just returns 6 articles."""
    client = DBClient()
    data = client.get_articles(count)
    posts = []
    for post in data:
        posts.append({  'image': './static/images/cat.jpg',
                        'title': post['title'],
                        'body': post['content'],
                        'updated': 'Last updated 3 mins ago. Also here is this broken time: ' + str(datetime.datetime.now() - post['datetime'])
                      #   Well, the time is right, but it's formatted really ugly...
                      })
    return posts

def get_keyword_news(keyword, count = 6):
    """"Returns a number of articles matching the keyword

    For now, it just returns 6 articles."""

    client = DBClient()
    data = client.get_articles(count)
    posts = []
    for post in data:
        posts.append({  'image': './static/images/cat.jpg',
                        'title': post['title'],
                        'body': post['content'],
                        'updated': 'Last updated 3 mins ago. Also here is this broken time: ' + str(datetime.datetime.now() - post['datetime'])
                      #   Well, the time is right, but it's formatted really ugly...
                      })
    return posts
