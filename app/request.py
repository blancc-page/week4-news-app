import urllib.request,json
import datetime
from .models import Source, Article


# Getting api key
api_key = None
# Getting the source base url
base_url = None
# Getting the article base url
article_base_url = None

def configure_request(create_app):
    global api_key,base_url,article_base_url
    api_key = create_app.config['API_KEY']
    base_url = create_app.config['SOURCES_BASE_URL']
    article_base_url= create_app.config['ARTICLE_BASE_URL']
     
    
def get_sources():
    """
    gets Json response
    """
    get_source_url = base_url.format(api_key)
    
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)
        
        source_results = None
        
        if get_source_response["sources"]:
            source_results_list = get_source_response["sources"]
            source_results = process_results(source_results_list)
            
            
    return source_results

def get_articles(id):
    """
    gets Json response
    """
    get_article_url = article_base_url.format(id,api_key)
    
    with urllib.request.urlopen(get_article_url) as url:
        article_data = url.read()
        article_response = json.loads(article_data)

        article_results = None
        
        
    if article_response["articles"]:
            article_results_list = article_response["articles"]
            article_results = process_articles(article_results_list)
            
    return article_results
            
    # return article_object
            
def process_results(source_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    source_results = []
    
    for source_item in source_list:
        id = source_item.get("id")
        name = source_item.get("name")
        desc = source_item.get("description")
        lang = source_item.get("language")
        
        if lang == "en":
            source_object = Source(id, name, desc, lang)
            source_results.append(source_object)
            
    return source_results

def process_articles(article_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    article_results = []
    
    for article_item in article_list:
        image = article_item.get("urlToImage")
        title = article_item.get("title")
        desc = article_item.get("description")
        url = article_item.get("url")
        date = datetime.datetime.strptime(article_item.get("publishedAt"), "%Y-%m-%dT%H:%M:%SZ")
        print(date)
        time = date.strftime("%d, %B %Y, %H:%M")
        source = article_item.get("source")
        
        if image != "null":
            article_object = Article(image, title, desc, url, time, source)
            article_results.append(article_object)
            
    return article_results
        
        
        