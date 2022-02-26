class Articles:
      '''
  class to define articles object
  '''
def __init__(self,urlToImage,title,description,url,time,content):
    self.urlToImage=urlToImage
    self.title=title
    self.description=description
    self.url=url
    self.time=time
    self.content=content

class Sources:
  def __init__(self,id,name,url):
    self.id=id
    self.name=name
    self.url=url