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
        self.new_article = Article("abc-news","ABC News","Lorem10","en")
        
    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_article.id, "abc-news")
        self.assertEqual(self.new_article.name, "ABC News")
        self.assertEqual(self.new_article.desc, "Lorem10")
        self.assertEqual(self.new_article.lang, "en")