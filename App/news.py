# from os import name
from flask import render_template
from App import app
from App.models.articles import Articles
from .request import  get_articles, get_source,sources

@app.route('/')
def index():
  '''
  Root page function that returns index page and its data
  '''
  # breakpoint()
  sources=get_source()
  #get news article
  fav_source=get_articles('sources')
  title='News_Blog'
  return render_template('index.html',title = title,Sources=fav_source,sources=sources)