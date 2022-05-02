from flask import render_template, request, redirect, url_for
from ..request import get_sources, get_articles
from . import main


@main.route("/")
def index():
    """
    View root page function that returns the index page and its data
    """
    title = 'Home - Welcome to News App'
    
    source = get_sources()
    
    return render_template("index.html", title = title, source = source)

@main.route("/source/<id>")
def article(id):
    """
    View article page function that returns the article details page
    """
    
    article = get_articles(id)
    title = f"{article[0].source['name']}"

    print(article[0].time)

    
    return render_template("article.html", article = article, title = title)
