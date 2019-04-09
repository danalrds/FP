class Grade():
    def __init__(self,studid,nrlab,prob,val):
        self._studid=studid
        self._nrlab=nrlab
        self._prob=prob
        self._val=val

    def getStudid(self):
        return int(self._studid)


    def getNrlab(self):
        return int(self._nrlab)


    def getProb(self):
        return int(self._prob)


    def getVal(self):
        return int(self._val)

    def __str__(self):
        return str(self.getStudid())+';'+str(self.getNrlab())+';'+str(self.getProb())+';'+str(self.getVal())