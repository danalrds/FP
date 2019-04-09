from sentclass import Sentence
class Interface():
    def __init__(self,control):
        self._control=control
    def printmenu(self):
        print("1.Add sentence")
        print("2.start game")
    def mainmenu(self):
        try:
            while True:
                self.printmenu()
                com=input("Enter command: ")
                if com=="1":
                    prop=self.readvalidSentence("Give sentence:")
                    sent=Sentence(prop)
                    self._control.add(sent)
                elif com=="2":
                    self._control.start()
                elif com=="0":
                    break
                else:
                    raise ValueError("Invalid command!")
        except ValueError as exc:
            print(exc)
    def readvalidSentence(self,ms):
        ok=False
        while ok==False:
            ok=True
            x=input(ms)
            lista=x.split(" ")
            i=0
            while i<len(lista):
                if lista[i]=="":
                    lista.pop(i)
                    i=i-1
                i+=1            
            if len(lista)==0:
                print("Sentence must have at least one word!")
                ok=False
            elif self._control.find(x)==True:
                print("Sentence already in list!")
                ok=False
            else:
                for d in lista:
                    if len(d)<3:
                        print("Any word has to have at least 3 letters!")
                        ok=False
                        break
        return x