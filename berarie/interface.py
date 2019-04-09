class Interface():
    def __init__(self,control):
        self._control=control
    def printmenu(self):
        print("1.Update price")
        print("2.Discount ")
        print("3.List all")
        print("0.Exit")
    def mainmenu(self):
        while True:
            try:
                self.printmenu()
                com=input("Enter command!")
                if com=="1":
                    name=input("Give name: ")
                    x=int(input("Give percent: "))
                    procent=x/100
                    self._control.updateprice(name,procent)
                elif com=="2":
                    tip=input("Give type: ")
                    self._control.updatebytype(tip)
                elif com=="3":
                    self._control.list()
                elif com=="0":
                    break
                else:
                    raise ValueError("Invalid command!")
            except Exception as exc:
                print(exc)