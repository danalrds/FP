import unittest
from tema.repository.Repo import *
from tema.domain.classes import *


class TestRepo(unittest.TestCase):


    def setUp(self):
        self._repo=StudentRepository()
    def testRepoStore(self):        
        #self.assertEqual(len(self._repo), 0)
        b=Student(11,'Bob')
        self._repo.add(b)
        self.assertEqual(len(self._repo),1)
        h=Student(2,'Harald')
        self._repo.add(h)
        self.assertEqual(len(self._repo),2)
        self.assertEqual(self._repo.find(2),h)
        self.assertEqual(self._repo.find(3),None)
        self._repo.delete(2)
        self.assertEqual(len(self._repo),1)
        self._repo.add(h)
    def testRepoRemove(self):
        b=Student(1,'Bob')
        self._repo.add(b)
        self.assertEqual(len(self._repo),1)
        h=Student(2,'Harald')
        self._repo.add(h)
        self._repo.remove(2)
        self.assertEqual(len(self._repo),1)
        self.assertRaises(RepositoryException, self._repo.delete, 3)
    def testRepoFind(self):
        b=Student(1,'Bob')
        
        self._repo.add(b)
        self.assertEqual(self._repo.find(1), b)
        self.assertEqual(self._repo.find(3),None)
    def testRepoUpdate(self):
        b=Student(1,'Bob')
        h=Student(1,'Harald')
        self._repo.add(b)
        self._repo.update(h)
        self.assertEqual(h.getName(),'Harald')
        q=self._repo.find(1)
        self.assertEqual(q.getName(),'Harald')
    
   