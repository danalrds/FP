from studentrepository import Repository
from studentrepository import GradeRepository
from studentclass import Student
from gradeclass import Grade
from copy import deepcopy
class Controller():
    def __init__(self,repo,graderepo):
        self._repo=repo
        self._graderepo=graderepo
    def getAll(self):
        return self._repo.getAll()
    def getAllGrades(self):
        return self._graderepo.getAllGrades()
    def find(self,id):
        for s in self.getAll():
            if s.getId()==id:
                return s
        return None
    def findbyname(self,name):
        for s in self.getAll():
            if s.getName()==name:
                return s
        return None
    def add(self,obj):
        id=obj.getId()
        if self.find(id)==None:
            self._repo.store(obj)
    def findgrade(self,id):
        for g in self.getAllGrades():            
            if g.getStudid()==id:
                return g
        return None
    def delete(self,obj):        
        id=obj.getId()
        if self.findgrade(id)==None:
            self._repo.remove(obj)
    def verif_prob(self,id):
        for g in self.getAllGrades():
            if g.getStudid()==id:
                return True
        return False
    def assign(self,student,prob):
        id=student.getId()       
        if self.verif_prob(id)==False:            
            studid=id
            nrlab=0
            value=0
            newgrade=Grade(studid,nrlab,prob,value)
            self._graderepo.store(newgrade)
            
        else:
            raise Exception("Student has already a problem assigned!")
    
    def assignlab(self,prob,lab):
        for s in self.getAll():
            id=s.getId()       
            if self.verif_prob(id)==False:            
                studid=id
                nrlab=lab
                value=0
                newgrade=Grade(studid,nrlab,prob,value)
                self._graderepo.store(newgrade)
            else:
                grade=self.findgrade(id)
                studid=id
                nrlab=lab
                prob=grade.getProb()
                value=0
                newgrade=Grade(studid,nrlab,prob,value)
                self._graderepo.update(grade,newgrade)
    def order(self):
        grades=self.getAllGrades()
        list=deepcopy(grades)
        list.sort(key=lambda x:x.getVal(), reverse=True)
        for l in list:
            print(str(l))
            
                