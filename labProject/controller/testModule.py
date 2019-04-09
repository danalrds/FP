'''
Created on Dec 1, 2016

@author: Imi
'''
import unittest

from controller.ClientControl import ClientController
from domain.clientClass import Client
from repository.repositoryClass import Repository, RepositoryException
from controller.MovieController import MovieController
from domain.movieClass import Movie
from controller.rentalController import RentalController
from domain.rentalClass import RentalValidator
from datetime import *
from domain.rentalClass import Rental
class TestClientController(unittest.TestCase):
    def setUp(self):
        repos=Repository()
        self._control=ClientController(repos)
    def testFilterClients(self):
        b=Client(1,'Bob')
        h=Client(2,'Harambe')
        self._control.addClient(b)
        self._control.addClient(h)
        self.assertEqual(len(self._control._repos), 2)
        self._control.removeClient(2)
        self.assertEqual(len(self._control._repos), 1)
        self._control.addClient(h)
        l=self._control.filterClients(1, None)
        self.assertEqual(len(l), 1)
        self.assertTrue(b in l)
        self.assertTrue(h not in l)
        l=self._control.filterClients(None, 'b')
        self.assertEqual(len(l), 2)
        l=self._control.filterClients(None, 'Har')
        self.assertTrue(len(l)==1 and h in l)
class TestMovieController(unittest.TestCase):
    def setUp(self):
        repo=Repository()
        self._control=MovieController(repo)
    def testMovieFilter(self):
        lotr=Movie(1,'LotR', 'short descr', 'fantasy')
        nsm=Movie(2,'NowYouSeeMe', 'another description', 'idk')
        self._control.addMovie(lotr)
        self._control.addMovie(nsm)
        l=self._control.filterMovies(1, None, None,None)
        self.assertTrue(len(l)==1 and lotr in l)
        l=self._control.filterMovies(None,'lOTr', None,None)   
        self.assertTrue(len(l)==1 and lotr in l and nsm not in l)
class TestRentalController(unittest.TestCase):
    def setUp(self):
        mrepo=Repository()
        crepo=Repository()
        rrepo=Repository()
        validator=RentalValidator()
        self._control=RentalController(rrepo,mrepo,crepo,validator)
    def testFilterRentals(self):
        b=Client(1,'Bob')
        lotr=Movie(1,'LotR', 'short descr', 'fantasy')
        rd='2016, 12, 20'
        dd='2016, 12, 24'
        self._control._MovieRepo.store(lotr)
        self._control._ClientRepo.store(b)
        rdate=datetime.strptime(rd, '%Y, %m, %d')
        ddate=datetime.strptime(dd, '%Y, %m, %d')
        rental=Rental(1,lotr,b,rdate,ddate,None)
        self._control.addRental(1, 1, 1, rdate, ddate)
        self.assertRaises(RepositoryException,self._control.addRental,2, 2, 1, rdate, ddate)
        self.assertEqual(len(self._control._RentalRepo),1)
        self.assertRaises(RepositoryException, self._control.returnMovie,2,ddate)
        self._control.returnMovie(1, ddate)
        self.assertTrue(self._control._RentalRepo.find(1).getReturnDate()!=None)
        