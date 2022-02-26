# from distutils.debug import DEBUG
from os import environ
# from instance.config import NEWS_API
NEWS_API = environ.get('NEWS_API')


class Config:
  '''
  General config parent class
  '''
  NEWS_API_BASE_URL='https://newsapi.org/v2/everything?q={}&sources&from=2022-01-31&sortBy=popularity&apiKey={}'
  NEW_NEWS='https://newsapi.org/v2/top-headlines/{}?apiKey={}'

class ProdConfig(Config):
  '''
  Prod onfig child class
  Arg:
    Config: Parent class with General configuration settings
  '''
  pass

class DevConfig(Config):
  '''
  Dev config child class 
  '''
  DEBUG=True