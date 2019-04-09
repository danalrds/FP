class Interface():
    def __init__(self,control):
        self._control=control
    def printmenu(self):
        print("1.Search by name")
        print("2.Make receipe")
        print("0.Exit")
    def mainmenu(self):
        stop=False
        while stop==False:
            try:
                self.printmenu()
                comm=input("Enter command:")
                if comm=="1":
                    name=input("Give substring: ")
                    for t in self._control.lookup(name):
                        print(str(t))
                elif comm=="2":
                    val=int(input("Give number: "))
                    lista=[]
                    for i in range(0,val):
                        name=input("medicine name: ")
                        lista.append(name)
                    medicamente=self._control.createreceipe(lista)
                    for m in medicamente:
                        print(str(m))
                    price=self._control.createreceipe2(lista)
                    print(price)
                elif comm=="0":
                    stop=True
                else:
                    raise ValueError("Invalid command!")
            except MemoryError as exc:
                print(exc)
                    