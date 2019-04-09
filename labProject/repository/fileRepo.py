'''
Created on Jan 11, 2017

@author: Imi
'''
class Repository():
    def __init__(self,name):
        self._file=name
        self._objects=[]
        self.__loadFromFile
    def __loadFromFile(self):
        try:
            f=open(self._file,'r')
            line=f.readline().strip()
            while line!="":
                lData=line.split(';')
                obj=object(lData[0],lData[1])
                line=f.readline().strip()
                self.store(obj)
        except IOError:
            raise Exception
        finally:
            f.close()
    def __storeToFile(self):
        f=open(self._file,'w')
        objList=self.getAll()
        for o in objList:
            #strobj->s+\n maybe write inside the for
            s='++'
        f.write(s)
        f.close()
    def store(self,id):
        obj=self.find(id)
        if obj==None:
            self._objects.append(obj)
        else:
            raise Exception('id used')
        self.__storeToFile()
    def find(self,id):
        for o in self._objects:
            if o.getId()==id:
                return o
        return None
    def delete(self,id):
        o=self.find(id)
        if o==None:
            raise Exception
        else:
            self._objects.remove(o)
        self.__storeToFile()
    def getAll(self):
        return self._objects
    def __len__(self):
        return len(self._objects)
    
rep=Repository('rep.')
rep.store(5)
print(rep.getAll())