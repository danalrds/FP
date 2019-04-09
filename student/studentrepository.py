from studentclass import Student
from gradeclass import Grade
import unittest
class Repository():
    def __init__(self,fname):
        self._objects=[]
        self._fname=fname
        self.__loadfromfile()
    def __loadfromfile(self):
        try:
            f=open(self._fname,"r")
            line=f.readline().strip()
            while line!='':
                d=line.split(';')
                student=Student(int(d[0]),d[1],d[2])
                self.store(student)
                line=f.readline().strip()
            
        except EOFError:
            raise Exception("wrong.")
        f.close()
    def store(self,object):
        self._objects.append(object)
        self.__storetofile()
    def remove(self,obj):
        self._objects.remove(obj)
        self.__storetofile()
    def getAll(self):
        return self._objects
    def __storetofile(self):
        f=open(self._fname,"w")
        for s in self._objects:
            f.write(str(s))
            f.write("\n")
        f.close()
        
class Test(unittest.TestCase):
    def setUp(self):
        self._repo=Repository("students.txt")

    def testName(self):
        list=self._repo.getAll()
        self.assertEqual(len(list),5)
        stud=Student('1','Kara','715')
        self._repo.store(stud)
        list=self._repo.getAll()
        self.assertEqual(list[5],stud)
        

class GradeRepository():
    def __init__(self,fname):
        self._grades=[]
        self._fname=fname
        self.__loadfromfile()
    def __loadfromfile(self):
        try:
            f=open(self._fname,"r")
            line=f.readline().strip()
            while line!='':
                d=line.split(';')
                grade=Grade(int(d[0]),int(d[1]),int(d[2]),int(d[3]))
                self.store(grade)
                line=f.readline().strip()
            
        except EOFError:
            raise Exception("wrong.")
        f.close()
    def store(self,object):
        self._grades.append(object)
        self.__storetofile()
    def getAllGrades(self):
        return self._grades
    def __storetofile(self):
        f=open(self._fname,"w")
        for s in self._grades:
            f.write(str(s))
            f.write("\n")
        f.close()
    def update(self,old,new):
        idx=self._grades.index(old)
        self._grades[idx]=new
        self.__storetofile()
        