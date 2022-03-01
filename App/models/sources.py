from xml.etree.ElementTree import Comment
from flask import render_template, request, redirect, url_for
# from request import news

class Sources:
    def __init__(self,id,name,url):
        self.id=id
        self.name=name
        self.url=url