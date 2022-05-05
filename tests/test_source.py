import unittest
from app.models import Source


class TestSource(unittest.TestCase):
    """
    Test class that defines test case for the Source class behaviours
    
    Args:
        unittests.TestCase: helps in creating test cases 
        
    """
    
    def setUp(self):
        """
        Set up method to run before each test case
        
        """
        self.new_source = Source("abc-news","ABC News","Lorem10","en")
        
    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_source.id, "abc-news")
        self.assertEqual(self.new_source.name, "ABC News")
        self.assertEqual(self.new_source.desc, "Lorem10")
        self.assertEqual(self.new_source.lang, "en")