import unittest
from  app .models import Blog

class BlogModelTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the Blog Model
    '''
    def setUp(self):
        '''
        setup method that runs before every test
        '''
        self.new_blog = Blog(Blog= 'checki man')
    def test_blog(self):
        self.assertTrue(self.test_blog is not None)