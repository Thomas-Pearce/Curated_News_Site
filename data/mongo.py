from pymongo import MongoClient
from config import get_config



db_conf = get_config()['DB']
DEFAULT_HOST = db_conf['HOST']
DEFAULT_PORT = db_conf['PORT']
DEFAULT_DB = db_conf['DB']


class DBClient(object):


    def __init__(self, host=DEFAULT_HOST, port=DEFAULT_PORT, db=DEFAULT_DB):
        """Returns a db connection

        :param host: string, optional
        :param port: int, optional
        :return: a db connection to the scallion db
        """
        self.__client = MongoClient(host, port)
        self.__db = self.__client.get_database(db)


    def is_initialized(self):
        """Returns True if there are a non-zero number of entries in the
        articles collection, otherwise returns False.

        :return: Boolean value
        """
        if self.__db.articles.count() == 0:
            return False
        else:
            return True


    def add_articles(self, data):
        """Takes a vector of dicts and adds them as articles to the connected db. Will not add duplicates.


        WARNING, this is from the Lexxe implementation, it requires modification.


        :param data: A vector of dicts
        """
        articles = self.__db.articles
        for article in data:
            if not articles.find_one({"docid": article["docid"]}):
                articles.insert_one(article)
            else:
                print(article["docid"] + ' is already in the db')


    def get_articles(self, n):
        return self.__db.articles.find().limit(n)


    def add_user(self, data):
        return NotImplementedError


    def get_user(self, key):
        return NotImplementedError