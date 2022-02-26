# from os import name
from flask import render_template
from app import app
from .request import Sources, get_articles, get_source

@app.route('/')
def index():
  '''
  Root page function that returns index page and its data
  '''
  # breakpoint()
  sourcez=get_source('sources')
  #get news article
  fav_source=get_articles('sources')
  title='News_Blog'
  return render_template('index.html',title = title,sources=fav_source,source=Sources)