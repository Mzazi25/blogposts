import unittest
from  app .models import User

class UserModelTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(password= 'Mzazi')
    def test_password_setter(self):
        self.assertTrue(self.new_user.password is not None)