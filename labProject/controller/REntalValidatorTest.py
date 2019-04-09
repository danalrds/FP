'''
Created on Dec 1, 2016

@author: Imi
'''
import unittest
from domain.rentalClass import RentalValidator, Rental
from domain.clientClass import Client
from domain.movieClass import Movie
from datetime import *
from domain.validatorEXception import ValidatorException

class Test(unittest.TestCase):


    def setUp(self):
        self._validator=RentalValidator()
    def testVAlidator(self):
        c=Client(1,'Bob')
        m=Movie(1,'Title','descr.', 'genre')
        rd='2016, 12, 2'
        dd='2016, 12, 12'
        rdate=datetime.strptime(rd, '%Y, %m, %d')
        ddate=datetime.strptime(dd, '%Y, %m, %d')
        r=Rental(1,m,c,rdate,ddate,None)
        try:
            self._validator.validate(r)
            self.assertTrue(1==1)
        except ValidatorException:
            self.assertTrue(1==2)
        dd='2016, 11, 1'
        ddate=datetime.strptime(dd, '%Y, %m, %d')
        r=Rental(1,m,c,rdate,ddate,None)
        try:
            self._validator.validate(r)
            self.assertTrue(1==2)
        except ValidatorException:
            self.assertTrue(1==1)
            '''
            assertRaises in place of that try-except stuff
            '''                                                                         
        self.assertRaises(TypeError, self._validator.validate, c)