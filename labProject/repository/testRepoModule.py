'''
Created on Dec 1, 2016

@author: Imi
'''
import unittest
from repository.repositoryClass import Repository, RepositoryException
from domain.clientClass import Client


class TestRepo(unittest.TestCase):


    def setUp(self):
        self._repo=Repository()
    def testRepoStore(self):
        self.assertEqual(len(self._repo), 0)
        b=Client(1,'Bob')
        self._repo.store(b)
        self.assertEqual(len(self._repo),1)
        h=Client(2,'Harambe')
        self._repo.store(h)
        self.assertEqual(len(self._repo),2)
        self.assertEqual(self._repo.find(2),h)
        self.assertEqual(self._repo.find(3),None)
        self._repo.delete(2)
        self.assertEqual(len(self._repo),1)
        self._repo.store(h)
    def testRepoRemove(self):
        b=Client(1,'Bob')
        self._repo.store(b)
        self.assertEqual(len(self._repo),1)
        h=Client(2,'Harambe')
        self._repo.store(h)
        self._repo.delete(2)
        self.assertEqual(len(self._repo),1)
        self.assertRaises(RepositoryException, self._repo.delete, 3)
    def testRepoFind(self):
        b=Client(1,'Bob')
        
        self._repo.store(b)
        self.assertEqual(self._repo.find(1), b)
        self.assertEqual(self._repo.find(3),None)
    def testRepoUpdate(self):
        b=Client(1,'Bob')
        h=Client(1,'Harambe')
        self._repo.store(b)
        self._repo.update(h)
        self.assertEqual(h.getName(),'Harambe')
        q=self._repo.find(1)
        self.assertEqual(q.getName(),'Harambe')
    
        
#testr=TestRepo()
#testr.setUp()
#testr.testRepoStore()
#testr.testRepoRemove()
