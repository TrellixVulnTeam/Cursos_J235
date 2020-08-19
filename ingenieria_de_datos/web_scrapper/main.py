import argparse
from common import config
import logging
logging.basicConfig(level=logging.INFO)
import news_page_object as news

logger = logging.getLogger(__name__)

def _news_scraper(news_site_uid):
    host = config()['news_sites'][news_site_uid]['url']
    logging.info('Beggining scraper for {}'.format(host))

    homepage = news.HomePage(news_site_uid, host)

    for link in homepage.article_links:
        print(link)

if __name__ == '__main__':
        parser = argparse.ArgumentParser(description='Receive the URL')

        #The choices are simply the options that user has available

        #The config() function returns a map so we access sites and shows the
        #keys of it
        news_site_choices = list(config()['news_sites'].keys())

        parser.add_argument('news_site',
                            help = 'The new sites you want to scrape',
                            type = str,
                            choices = news_site_choices)

        args = parser.parse_args()

        #We call the function above and pass as an argument the news site that
        #user had chosen
        _news_scraper(args.news_site)
