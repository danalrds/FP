from classes import Film
class Interface():
    def __init__(self,control):
        self._control=control
    def printmenu(self):
        print("1.List all")
        print("2.Update film")
        print("0.Exit")
    def mainmenu(self):
        while True:
            try:
                self.printmenu()
                com=input("Enter command: ")
                if com=="1":
                    for t in self._control.getAll():
                        print(str(t))
                elif com=="2":
                    id=self.readId("Give id: ")
                    name=self.readName("Give name: ")
                    price=self.readPrice("Give price: ")
                    places=self.readPlaces("Give places: ")
                    old=self._control.findbyid(id)
                    new=Film(id,name,price,places)
                    self._control.actualizeaza(old,new)
                elif com=="0":
                    break
                else:
                    raise ValueError("Invalid command!")                        
            except Exception as exc:
                print(str(exc))
    
    def readId(self,ms):
        ok=True
        while ok==True:
            ok=False
            id=int(input(ms))
            obj=self._control.findbyid(id)
            if obj==None:
                ok=True
                print("Inexistent id!")
            else:
                return id
    def readName(self,ms):
        ok=True
        while ok==True:
            ok=False
            name=input(ms)            
            if len(name)>30:
                ok=True
                print("len name must be <=30!")
            else:
                return name
    
    def readPrice(self,ms):
        ok=True
        while ok==True:
            ok=False
            price=float(input(ms))            
            if price<10 or price>20:
                ok=True
                print("price must be in [10,20]!")
            else:
                return price
    def readPlaces(self,ms):
        ok=True
        while ok==True:
            ok=False
            places=int(input(ms))            
            if places<0 or places>100:
                ok=True
                print("places must be in [0,100]!")
            else:
                return places
    