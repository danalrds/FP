from dictionary import Dictionary
from repository import Repository

class Controller():
    def __init__(self,repo):
        self._repo=repo
    def getAll(self):
        return self._repo.getAll()
    def add(self,object):
        self._repo.store(object)
    def check(self,lang,phrase):
        i=0        
        cuv = phrase.split(" ")        
        while i<len(cuv):
            if cuv[i]=='':
                cuv.pop(i)
                i=i-1
            i+=1        
        for i in range(0,len(cuv)):
            cuvant=cuv[i]
            if self.find(lang,cuvant)==None:
                print(cuvant)
    def find(self,lang,cuvv):
        for d in self.getAll():
            if d.getLang()==lang:
                if d.getWord()==cuvv:
                    return d
        return None
    def find2(self,cuvv):
        for d in self.getAll():
            if d.getWord()==cuvv:
                return d
        return None
    def spell(self,entrance,exit):
        try:
            f=open(entrance,'r')
            ex=open(exit,'w')
            prop=f.read().strip()
            cuv = prop.split(" ")  
            i=0      
            while i<len(cuv):
                if cuv[i]=='':
                    cuv.pop(i)
                    i=i-1
                i+=1 
            for i in range(0,len(cuv)):
                cuvant=cuv[i]
                if len(cuv[i])>2:                    
                    if self.find2(cuvant)==None:
                        cuvant="{"+cuvant+"}"
                ex.write(cuvant)
                ex.write(" ")
            ex.close()
            f.close()
        except EOFError:
             raise ControllerException("wrong!")   

class ControllerException(Exception):
    def __init__(self,mes):
        self._mes=mes
    def __str__(self):
        return str(self._mes)