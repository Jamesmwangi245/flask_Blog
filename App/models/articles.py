class Articles:
    def __init__(self,id,name,author,description,url,urlToImage,publishedAt,content):
        self.id=id
        self.name=name
        self.author=author
        self.description=description
        self.url=url
        self.urlToImage=urlToImage
        self.publishedAt=publishedAt
        self.content=content

class Sources:
    def __init__(self,id,name,url):
        self.id=id
        self.name=name
        self.url=url