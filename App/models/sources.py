from xml.etree.ElementTree import Comment
from flask import render_template, request, redirect, url_for
# from request import news

class Sources:
    def __init__(self,id,name,author,title,description,url,urlToImage,publishedAt,content):
            self.id=id
            self.name=name
            self.author=author
            self.title=title
            self.description=description
            self.url=url
            self.urlToImage=urlToImage
            self.publishedAt=publishedAt
            self.content=content
