import unittest
from  app .models import Comment

class CommentModelTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the Pitch Model
    '''
    def setUp(self):
        '''
        setup method that runs before every test
        '''
        self.new_comment = Comment(Pitch= 'Mzazicaleb')
    def test_comment(self):
        self.assertTrue(self.test_comment is not None)