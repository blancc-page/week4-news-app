class Article:
    '''
    Article class to define Article Objects
    '''

    def __init__(self,urlToImage, title, description,url, publishedAt, source):
        self.image = urlToImage
        self.title = title
        self.desc = description
        self.url = url
        self.time = publishedAt
        self.source = source