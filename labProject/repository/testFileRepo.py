'''
Created on Dec 12, 2016

@author: Imi
'''
import unittest
from repository.ClientFileRepository import ClientFileRepository,\
    FileRepoException
from domain.clientClass import Client
from repository.repositoryClass import RepositoryException, Repository
from repository.movieFileRepository import MovieFileRepository
from domain.movieClass import Movie
from repository.rentalFileRepository import RentalFileREpository
from domain.rentalClass import Rental
from datetime import *
class TestClientFileRepo(unittest.TestCase):
    def setUp(self):
        self._clientFRepo=ClientFileRepository('C:/Users/Imi/Desktop/testC.txt')
    def testAdd(self):
        bob=Client(1,'bob')
        self._clientFRepo.clearAll()
        self._clientFRepo.store(Client(1,'bobbbby'))
        self.assertTrue(len(self._clientFRepo.getAll())==1)
        self.assertRaises(RepositoryException,self._clientFRepo.store,bob)
        self._clientFRepo.clearAll()
    def testDelete(self):
        bob=Client(1,'bob')
        self._clientFRepo.clearAll()
        self._clientFRepo.store(Client(1,'bobbbby'))
        self._clientFRepo.delete(1)
        self.assertEqual(len(self._clientFRepo.getAll()), 0)
        self.assertRaises(RepositoryException,self._clientFRepo.delete,1)
    def testUpdate(self):
        bob=Client(1,'UpdatedBob')
        self._clientFRepo.clearAll()
        self._clientFRepo.store(Client(1,'bobbbby'))
        self._clientFRepo.update(bob)
        self.assertEqual(self._clientFRepo.find(1).getName(), 'UpdatedBob')
        self.assertRaises(RepositoryException,self._clientFRepo.update,Client(2,'no'))
class TestMovieFileRepo(unittest.TestCase):
    def setUp(self):
        self._movieFRepo=MovieFileRepository('C:/Users/Imi/Desktop/testC.txt')
    def testAddMovie(self):
        mov=Movie(1,'title','desc','genre')
        self._movieFRepo.clearAll()
        self._movieFRepo.store(Movie(1,'bobbbby','desc','genre'))
        self.assertTrue(len(self._movieFRepo.getAll())==1)
        self.assertRaises(RepositoryException,self._movieFRepo.store,mov)
        self._movieFRepo.clearAll()
    def testDelete(self):
        mov=Movie(1,'title','desc','genre')
        self._movieFRepo.clearAll()
        self._movieFRepo.store(Movie(1,'bobbbby','desc','genre'))
        self._movieFRepo.delete(1)
        self.assertEqual(len(self._movieFRepo.getAll()), 0)
        self.assertRaises(RepositoryException,self._movieFRepo.delete,1)
    def testUpdate(self):
        mov=Movie(1,'title','desc','genre')
        self._movieFRepo.clearAll()
        self._movieFRepo.store(Movie(1,'bobbbby','desc','genre'))
        self._movieFRepo.update(mov)
        self.assertEqual(self._movieFRepo.find(1).getTitle(), 'title')
        self.assertRaises(RepositoryException,self._movieFRepo.update,Movie(2,'no','n','n'))
class TestRentalFileRepo(unittest.TestCase):
    def setUp(self):
        mRepo=Repository()
        cRepo=Repository()
        self._rentalFRepo=RentalFileREpository(mRepo,cRepo,'C:/Users/Imi/Desktop/testC.txt')
    def testAdd(self):
        self._rentalFRepo.clearAll()
        mov=Movie(1,'title','desc','genre')
        bob=Client(1,'UpdatedBob')
        self._rentalFRepo._clientRepo.store(bob)
        self._rentalFRepo._movieRepo.store(mov)
        rental=Rental(1,mov,bob,datetime.strptime('2016, 12, 15','%Y, %m, %d'),datetime.strptime('2016, 12, 19','%Y, %m, %d'),None)
        self._rentalFRepo.store(rental)
        self.assertTrue(len(self._rentalFRepo)==1)
        rental=Rental(1,mov,bob,datetime.strptime('2016, 12, 15','%Y, %m, %d'),datetime.strptime('2016, 12, 19','%Y, %m, %d'),None)
        self.assertRaises(RepositoryException,self._rentalFRepo.store,rental)
    def testDelete(self):
        self._rentalFRepo.clearAll()
        mov=Movie(1,'title','desc','genre')
        bob=Client(1,'UpdatedBob')
        rental=Rental(1,mov,bob,datetime.strptime('2016, 12, 15','%Y, %m, %d'),datetime.strptime('2016, 12, 19','%Y, %m, %d'),None)
        self._rentalFRepo.store(rental)
        self._rentalFRepo.delete(1)
        self.assertTrue(len(self._rentalFRepo)==0)
        self.assertRaises(RepositoryException,self._rentalFRepo.delete,2)
        
        
        
    
        
        
        