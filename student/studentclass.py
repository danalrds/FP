class Student():
    def __init__(self,id,name,group):
        self._id=id
        self._name=name
        self._group=group

    def getId(self):
        return int(self._id)


    def getName(self):
        return self._name


    def getGroup(self):
        return self._group

    def __str__(self):
        return str(self.getId())+';'+str(self.getName())+';'+str(self.getGroup())
    
