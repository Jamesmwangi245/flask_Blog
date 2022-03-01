# from newsapi import NewsApiClient
from App import app
import urllib.request,json

from App.articles_test import Articles
from App.models.articles import Articles
from .models import sources, articles

articles=articles.Articles
sources=sources.Sources


#Getting api key
api_key=app.config['NEWS_API_KEY']

#Getting the news articles base url
base_url=app.config["NEWS_API_BASE_URL"]
base2_url=app.config["NEW_BLOGS"]


def get_articles(sources):
  '''
  Func that gets the json response to url request
  # '''
  get_articles_url=base_url.format(sources,api_key)

  with urllib.request.urlopen(get_articles_url) as url:
    get_articles_data=url.read()
    get_articles_res=json.loads(get_articles_data)

    article_results = None

    if get_articles_res['articles']:
      article_results_list=get_articles_res['articles']
      article_results=process_results(article_results_list)

  return article_results      



def process_results(articles_list):
  '''
  Processes results and transform them to a list of objects
  Arg:
    articles_list:list of dictionaries that contain movie details
  '''
  article_results=[]
  for article_item in articles_list:
        id=article_item.get('id')
        name=article_item.get('name')
        author=article_item.get('author')
        description=article_item.get('description')
        url=article_item.get('url')
        urlToImage=article_item.get('urlToImage')
        title=article_item.get('title')
        publishedAt=article_item.get('publishedAt')
        content=article_item.get('content')


        if urlToImage:
          article_object=Articles(id,name,author,description,url,urlToImage,publishedAt,content)
          article_results.append(article_object)

  return article_results



def get_source():
      # get_source_url=base2_url.format(sources,api_key)
  
  with urllib.request.urlopen('https://newsapi.org/v2/top-headlines/sources?apiKey=4fc66dc1f39848ecab196c4806c87b40') as url:
    get_source_data=url.read()
    get_source_res=json.loads(get_source_data)

    source_results = None
    
    if get_source_res['sources']:
      source_results_list=get_source_res['sources']
      source_results=process_result(source_results_list)

  return source_results     

def process_result(source_list):
  '''
  Processes results and transform them to a list of objects
  Arg:
    articles_list:list of dictionaries that contain movie details
  '''
  source_results=[]
  for source_item in source_list:
    id=source_item.get('id')
    name=source_item.get('name')
    url=source_item.get('url')
    

    if id:
      source_object=sources(id,name,url)
      source_results.append(source_object)

  return source_results 
