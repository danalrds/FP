'''
Created on 16 dec. 2017

@author: User
'''
import unittest
class Book:
    def __init__(self,id,name): 
        self._id=id
        self._name=name

    def get_id(self):
        return self._id


    def get_name(self):
        return self._name


    def set_id(self, value):
        self._id = value


    def set_name(self, value):
        self._name = value    

    
class Test(unittest.TestCase):
    def testName(self):
        pass


