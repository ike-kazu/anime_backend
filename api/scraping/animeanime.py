import requests
from bs4 import BeautifulSoup
import api.schemas.article as article_schema

base_url = 'https://animeanime.jp'
url = 'https://animeanime.jp/category/news/latest/latest/'


def getArticle():
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    return soup


def scraping():
    soup = getArticle()
    articles_information = []

    for one_article in soup.select('section.item--cate-news'):
        article_information: article_schema.ArticleCreate = {
            "articleURL": base_url + one_article.find('a').get('href'),
            "imageURL": base_url + one_article.find('img').get('src'),
        }
        articles_information.append(article_information)

    return articles_information