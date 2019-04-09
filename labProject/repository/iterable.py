'''
'''
class Iterable:
    def __init__(self):
        self._data = []

    def append(self, o):
        self._data.append(o)

    def __iter__(self):
        self._iterPoz = 0
        
        return self
    def index(self,element):
        
        return self._data.index(element)
    def __delitem__(self,poz):
        del self._data[poz]
        
        #return idx
    def __setitem__(self,idx,new):
        self.data[idx]=new
    def __getitem__(self,poz):
        return self._data[poz]
    
    def remove(self,element):
        idx=self._data.index(element)
        del self._data[idx]
    
    def replace(self,old, new):
        idx=self._data.index(old)
        self._data[idx]=new
    
    def insert(self,poz, element):
        self._data[poz]=element
        
    def __next__(self):
        
        if self._iterPoz >= len(self._data):
            raise StopIteration()
        rez = self._data[self._iterPoz]
        self._iterPoz = self._iterPoz + 1
        return rez

    def __len__(self):
        return len(self._data)
    def __str__(self):
        s=''
        for e in self._data:
            s+=str(e)
        return s
    
    def gnome(self,accept):
        i=0
        while i<len(self._data)-1:
            if accept(self._data[i],self._data[i+1]):
                i+=1
            else:
                t=self._data[i]
                self._data[i]=self._data[i+1]
                self._data[i+1]=t
            if i-1<0:
                i=0
    def filter(self,accept):
        filtered=[]
        for i in range (len(self._data)):
            if accept(self._data[i]):
                filtered.append(self._data)
        return filtered
    
    
    
    
def filterList(l,accept):
    res=[]
    for i in range(len(l)):
        if accept(l[i]):
            res.append(l[i])
            
    return res
def gnomeSort(l, accept):
    i=0
    while i<len(l)-1:
        if accept(l[i],l[i+1]):
            t=l[i]
            l[i]=l[i+1]
            l[i+1]=t
            i-=1
            if i-1<0:
                i=0
        else:
            i+=1
def accept(x,y):
    return x>y
l=[5,2,3,1,4]
gnomeSort(l,accept)
print(l)
        
            
            
            
            
   
                