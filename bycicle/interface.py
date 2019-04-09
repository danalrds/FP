class Interface:
    def __init__(self,controller):
        self._control=controller
    def printmenu(self):
        print("1.List bycicles")
        print("2.Reduce price")
        print("0.Exit")
    def mainmenu(self):
        stop=False
        while stop==False:
            try:
                self.printmenu()
                comm=input("Enter command: ")
                if comm=="1":
                    for p in self._control.listall():
                        print(p)
                elif comm=="2":
                    type=input("Enter the type you want to reduce: ")
                    percent=self.readValidPercent("Enter percent: ")
                    percent=percent/ 100                    
                    self._control.reduceprice(type,percent)
                elif comm=="0":
                    stop=True
                else:
                    raise ValueError("Invalid command! ")
            except Exception as e:
                print(e)
    @staticmethod
    def readValidPercent(ms):
        percent=None
        while percent==None:
            try:
                percent=int(input(ms))
                if percent<=0 or percent>=100:
                    percent=None
                    raise ValueError
            except ValueError:
                print('Please enter a valid percent')
        return percent