from datetime import datetime
date="19.07"
data=date.split(".")
print(data)
new='2018-'+data[1]+'-'+data[0]+" 00:00:00"
dt_obj = datetime.strptime(new, "%Y-%m-%d %H:%M:%S")
print (dt_obj)




date_str = "2008-11-10 17:53:59"
dt_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print (dt_obj)

class Student():
    def __init__(self,id,nume,nota):
        self._id=id
        self._nume=nume
        self._nota=nota 

    def getId(self):
        return self._id


    def getNume(self):
        return self._nume


    def getNota(self):
        return self._nota
    def __str__(self):
        return str(self._id)+";"+str(self._nume)+";"+str(self._nota)
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
                line=f.readline().strip()
        except EOFError:
            raise Exception("Wrong!")