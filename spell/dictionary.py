import unittest
from pip._vendor.requests.packages.chardet import langbulgarianmodel
class Dictionary():
    def __init__(self,id,lang,word):
        self._id=id
        self._lang=lang
        self._word=word

    def getId(self):
        return int(self._id)


    def getLang(self):
        return self._lang


    def getWord(self):
        return self._word

    def __str__(self):
        return str(self.getId())+";"+str(self.getLang())+";"+str(self.getWord())
class Test(unittest.TestCase):


    def testDictionary(self):
        d=Dictionary(1,'Ro','farfurie')
        self.assertEqual(d.getId(),1)
        self.assertEqual(d.getLang(),'Ro')
        self.assertEqual(d.getWord(),'farfurie')