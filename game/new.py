'''
Created on 7 dec. 2017

@author: User
'''
def carcmp(a,b):
    return a.getmake()>b.getmake
def filter(data,acceptance):
    res=[]
    for i in data:
        if acceptance(i):
            res.append(i)
        return i
def acceptance(car):
    return car.getmake()=="Audi"
class mylist:
    def __init__(self):  
        self.__data=[]
    def getitem(self):
        pass
    def __next__(self):
        pass
    def __inter__(self):
        pass
    def sort(self,list,comparison):
        pass
    
    '''//x,y=y,x '''