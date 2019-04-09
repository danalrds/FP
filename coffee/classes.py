class Coffee():
    def __init__(self,name,country,price):
        self._name=name
        self._country=country
        self._price=price

    def getName(self):
        return self._name


    def getCountry(self):
        return self._country


    def getPrice(self):
        return self._price
    def __str__(self):
        return str(self.getName())+";"+str(self.getCountry())+";"+str(self.getPrice())

        