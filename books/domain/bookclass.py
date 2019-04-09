import unittest
class Book:
    def __init__(self,id,title,author):
        self._id=id
        self._title=title
        self._author=author
    def getId(self):
        return self._id
    def getTitle(self):
        return self._title
    def getAuthor(self):
        return self._author
    def setTitle(self,title):
        self._title=title
    def setAuthor(self,author):
        self._author=author   
    def __str__(self):
        return "id: "+str(self.getId())+" title: "+str(self.getTitle())+" author: "+str(self.getAuthor()) 
class testBook(unittest.TestCase):
    def testbook(self):
        b=Book(3,"Gone with the wind","Margaret Mitchell")
        self.assertEqual(b.getId(),3)
        self.assertEqual(b.getTitle(),"Gone with the wind")
        self.assertEqual(b.getAuthor(),"Margaret Mitchell")
        b.setTitle("La Tormenta")
        b.setAuthor("Alistair Mclean")
        self.assertEqual(b.getAuthor(),"Alistair Mclean")
        self.assertEqual(b.getTitle(),"La Tormenta")
        self.assertEqual(b.__str__(),"id: 3 title: La Tormenta author: Alistair Mclean")

