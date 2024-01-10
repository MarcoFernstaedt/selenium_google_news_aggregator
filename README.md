# Google News Scraper

## Overview

This project is a web scraper developed in Python using Selenium. It's designed to extract news articles from Google News, capturing both the text and the links of each article.

## Features

- Scrapes news articles from Google News.
- Retrieves the article text and associated links.
- Customizable to scrape a specific number of articles.

## Prerequisites

- Python
- Selenium
- A WebDriver compatible with your preferred browser (e.g., ChromeDriver for Google Chrome).

## Installation

### Prerequisites

- Python 3.x
- Selenium
- A WebDriver (e.g., ChromeDriver for Google Chrome)

### Setting up Python and Selenium

1. **Install Python**: If not already installed, download and install Python from [python.org](https://www.python.org/downloads/).

2. **Install Selenium**: Open your command line interface and run:
   ```bash
    pip install selenium
   '''

## Usage
1. Import the `GoogleScraper` class from the script.
2. Initialize the class with the URL of the news site (e.g., Google News) and the maximum number of articles to scrape.
3. Call the `scrape` method to start scraping the news articles.
4. Use the `display_articles` method to output the results.

Example:
```python
from google_scraper import GoogleScraper

scraper = GoogleScraper('https://google.com/news', max_articles=5)
scraper.scrape()
scraper.display_articles()

