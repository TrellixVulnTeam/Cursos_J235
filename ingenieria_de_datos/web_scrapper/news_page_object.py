import requests
import bs4
from common import config

#Creating a class acording Page Object Pattern
class HomePage:

    def __init__(self, news_site_uid, url):
        self._config = config()['news_sites'][news_site_uid]
        self._html = None
        #Acceding the queries of the config() function
        self._queries = self._config['queries']

        self._visit(url)

    @property
    def article_links(self):
        link_list = []

        #_select returns a list
        for link in self._select(self._queries['homepage_article_links']):
            link_list.append(link)
        return link_list

    #Selecting... This helps to obtain info of the parsed document
    def _select(self, query_string):
        return self._html.select(query_string)

    def _visit(self, url):
        response = requests.get(url)

        #This method raise an error if the solicitud fails
        response.raise_for_status()

        self._html = bs4.BeautifulSoup(response.text, 'html.parser')
