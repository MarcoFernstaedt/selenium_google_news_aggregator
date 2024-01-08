from selenium import webdriver
from selenium.webdriver.common.by import By

class GoogleScraper:
    def __init__(self, url, max_articles=5):
        """
        Initialize the scraper with a URL and a maximum number of articles to scrape.
        :param url: URL of the news site.
        :param max_articles: Maximum number of articles to scrape.
        """
        self.url = url
        self.max_articles = max_articles
        self.driver = webdriver.Chrome()
        self.news_articles = []

    def scrape(self):
        """
        Scrape the news articles from the specified URL.
        """
        self.driver.get(self.url)
        self.driver.implicitly_wait(5)
        article_data = self.driver.find_elements(by=By.CLASS_NAME, value='KDoq1')

        for article in article_data:
            if len(self.news_articles) < self.max_articles:
                newArticle = {
                    'article_text': article.text,
                    'article_links': article.get_attribute('href')
                }
                self.news_articles.append(newArticle)
            else:
                break

        self.driver.quit()

    def display_articles(self):
        """
        Display the scraped articles.
        """
        for count, article in enumerate(self.news_articles, 1):
            print(f'{count}. {article}')

# Usage
scraper = GoogleScraper('https://google.com/news')
scraper.scrape()
scraper.display_articles()
