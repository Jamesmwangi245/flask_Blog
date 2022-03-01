import os


# # from distutils.debug import DEBUG
# from distutils.command.config import config
# from os import environ
# # from instance.config import NEWS_API
# NEWS_API = environ.get('NEWS_API')


class Config:
  '''
  General config parent class
  '''
  NEWS_API_BASE_URL='https://newsapi.org/v2/everything?q=bitcoin&apiKey=4fc66dc1f39848ecab196c4806c87b40'
  NEW_BLOGS='https://newsapi.org/v2/top-headlines?country=us&apiKey=4fc66dc1f39848ecab196c4806c87b40'
  NEWS_API_KEY='4fc66dc1f39848ecab196c4806c87b40'

class ProdConfig(Config):
  '''
  Prod onfig child class
  Arg:
    Config: Parent class with General configuration settings
  '''
  pass

class DevConfig(Config):
 DEBUG=True

config_options = {
  'development': DevConfig,
  'production': ProdConfig
}