class Film():
    def __init__(self,id,name,price,places):
        self._id=id
        self._name=name
        self._price=price
        self._places=places

    def getId(self):
        return int(self._id)


    def getName(self):
        return self._name


    def getPrice(self):
        return float(self._price)


    def getPlaces(self):
        return int(self._places)
    def __str__(self):
        return str(self.getId())+";"+str(self.getName())+";"+str(self.getPrice())+";"+str(self.getPlaces())
