from flask import render_template, request, redirect, url_for
from app import create_app
from ..request import get_sources
# from ..models import review
# from .forms import ReviewForm
from . import main

@main.route("/")
def index():
    """
    View root page function that returns the index page and its data
    """
    title = 'Home - Welcome to News App'
    
    source = get_sources()
    
    print("ww")
    
    return render_template("index.html", title = title, source = source)
