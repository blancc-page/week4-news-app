from flask import render_template, request, redirect, url_for
from app import create_app
from ..request import get_sources, get_articles
# from ..models import Article
# from .forms import ReviewForm
from . import main
import datetime

# Article = article.Article

@main.route("/")
def index():
    """
    View root page function that returns the index page and its data
    """
    title = 'Home - Welcome to News App'
    
    source = get_sources()
    # print(source)
    
    return render_template("index.html", title = title, source = source)

@main.route("/source/<id>")
def article(id):
    """
    View article page function that returns the article details page
    """
    
    article = get_articles(id)
    title = f"{article[0].title}"
    # message = "published at {:%A, %B d%, %Y}."
    # dateTime = message.format(time)
    print(article[0].time)
    # print(article[0].source)
    # dt = article[0].time
    # time = dt.datetime.strptime(article[0]["publishedAt"], "%Y-%m-%dT%H:%M%SZ").date()
    
    return render_template("article.html", article = article, title = title)
