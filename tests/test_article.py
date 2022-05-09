import unittest
from app.models import Article


class TestArticle(unittest.TestCase):
    """
    Test class that defines test case for the Article class behaviours
    
    Args:
        unittests.TestCase: helps in creating test cases 
        
    """
    
    def setUp(self):
        """
        Set up method to run before each test case
        
        """
        self.new_article = Article(
        "https://ichef.bbci.co.uk/news/1024/branded_news/C7A9/production/_124631115_dmytro.png",
        "Ukraine war: 'If this is true, then I am also a Nazi'",
        "Holocaust survivors in the Ukrainian city of Uman feel insulted by Russian claims to be fighting Nazis.",
        "http://www.bbc.co.uk/news/world-europe-61361827",
        "2022-05-09T07:52:17.5346426Z",
        "BBC News")
        
    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_article.image, "https://ichef.bbci.co.uk/news/1024/branded_news/C7A9/production/_124631115_dmytro.png")
        self.assertEqual(self.new_article.title, "Ukraine war: 'If this is true, then I am also a Nazi'")
        self.assertEqual(self.new_article.desc, "Holocaust survivors in the Ukrainian city of Uman feel insulted by Russian claims to be fighting Nazis.")
        self.assertEqual(self.new_article.url, "http://www.bbc.co.uk/news/world-europe-61361827")
        self.assertEqual(self.new_article.publishedAt, "2022-05-09T07:52:17.5346426Z")
        self.assertEqual(self.new_article.source, "BBC News")















        CAN YOU HEAR ME???