class Bear():
    def __init__(self,name,type,price):
        self._name=name
        self._type=type
        self._price=price

    def getName(self):
        return self._name


    def getType(self):
        return self._type


    def getPrice(self):
        return float(self._price)

    def __str__(self):
        return str(self.getName())+","+str(self.getType())+","+str(self.getPrice())
    