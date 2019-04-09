from texttable import Texttable
from random import randint
import unittest
class Test(unittest.TestCase):    
    def testRepo(self):
        board=Board()
        self.__board=board
        self.__board=[[5,5,5,5,0,0],
               [-6,-6,-6,-6,0,0],
               [0,0,0,0,0,0],
               [0,0,0,0,0,0],
               [0,0,0,0,0,0],
               [0,0,0,0,0,0]]
        self.__board.makemoveai()
        self.assertEqual(self.__board==[[5,5,5,5,-6,0],
               [-6,-6,-6,-6,0,0],
               [0,0,0,0,0,0],
               [0,0,0,0,0,0],
               [0,0,0,0,0,0],
               [0,0,0,0,0,0]])
        p=Point(1,1,'x')
        ok=self.__board.validare(p)
        self.assetEqual(ok,True)
        p=Point(5,5,'o')
        ok=self.__board.validare(p)
        self.assetEqual(ok,True)
        p=Point(5,9,'o')
        ok=self.__board.validare(p)
        self.assetEqual(ok,False)
        
class Point():
    def __init__(self,x,y,simbol):
        self._x=x 
        self._y=y
        self._simbol=simbol

    def getx(self):
        return self._x


    def gety(self):
        return self._y


    def getsimbol(self):
        return self._simbol
class Board():
    def __init__(self):
        self._board=[[0,0,0,0,0,0],
               [0,0,0,0,0,0],
               [0,0,0,0,0,0],
               [0,0,0,0,0,0],
               [0,0,0,0,0,0],
               [0,0,0,0,0,0]]

    def show(self):        
        table = Texttable()    
        for i in range(0,6): 
            vect=[]
            for j in range(0,6):
                if self._board[i][j]==0:
                    vect.append(" ")
                if self._board[i][j]==5:
                    vect.append("x")   
                if self._board[i][j]==-6:
                    vect.append("o")   
            table.add_row(vect)
        return table 
    def encode(self,number):
        if number==5:
            return 'x'
        if number ==0:
            return ' '
        if number ==-6:
            return 'o'
    def validare(self,point):
        if point.getx()>=0 and point.getx()<6 and point.gety()>=0 and point.gety()<6:
            if self._board[point.getx()][point.gety()]==0:
                return True
        return False
    def makemove(self,point):
        x=point.getx()
        y=point.gety()
        simbol=point.getsimbol()
        #print(x,y,simbol)
        b=self._board
        if simbol=='x':
            b[x][y]=5
        else:
            b[x][y]=-6
    def availablemoves(self):       
        b=self._board
        moves=[]
        for l in range(0,6):
            for c in range(0,6):
                if b[l][c]==0:
                    moves.append(Point(l,c,' '))
        return moves    
    ''' makemove ai if ai can stop the n-1 trial of win it does  otherwise it moves randomly'''
    def makemoveAi(self):
        try:
            point=self.possibleWin()
        except Exception as exc:
            print(exc)
            point=None
        if point!=None:
            self.makemove(point)
        else:
            
            avmoves=[]
            avmoves=self.availablemoves()  
            idx=randint(0,len(avmoves)-1)
            point=avmoves[idx]        
            x=point.getx()
            y=point.gety()
            idx=randint(0,1)
            simboluri=['o','x']
            simbol=simboluri[idx]
            newpoint=Point(x,y,simbol)
        
            self.makemove(newpoint)
    def isGameWon(self):
        b=self._board        
        for k in range(0,6):
            for i in range(0,2):
                s=0
                for j in range(i,i+5):
                    s+=b[k][j]
                if s in [25,-30]:
                    return True
        for col in range(0,6):
            for i in range(0,2):
                s=0
                for j in range(i,i+5):
                    s+=b[j][col]
                if s in [25,-30]:
                    return True  
        '''prima diagonala '''  
        s=b[1][0]+b[2][1]+b[3][2]+b[4][3]+b[5][4]
        if s in [25,-30]:
            return True
        s=b[0][0]+b[1][1]+b[2][2]+b[3][3]+b[4][4]
        if s in [25,-30]:
            return True
        s=b[1][1]+b[2][2]+b[3][3]+b[4][4]+b[5][5]
        if s in [25,-30]:
            return True
        s=b[0][1]+b[1][2]+b[2][3]+b[3][4]+b[4][5]
        if s in [25,-30]:
            return True
        ''' a doua diagonala'''
        s=b[0][4]+b[1][3]+b[2][2]+b[3][1]+b[4][0]
        if s in [25,-30]:
            return True
        s=b[0][5]+b[1][4]+b[2][3]+b[3][2]+b[4][1]
        if s in [25,-30]:
            return True
        s=b[1][4]+b[2][3]+b[3][2]+b[4][1]+b[5][0]
        if s in [25,-30]:
            return True
        s=b[1][5]+b[2][4]+b[3][3]+b[4][2]+b[5][1]
        if s in [25,-30]:
            return True
        return False
    ''' the ai possible win if the player can win with the next move the ai has to stop him'''
    def possibleWin(self):
        b=self._board        
        for k in range(0,6):
            for i in range(0,2):
                s=0
                for j in range(i,i+5):
                    s+=b[k][j]
                if s in [20,-24]:
                    for j in range(i,i+5):
                        if b[k][j]==0:
                            if s==20:
                                simbol="o"
                            else:
                                simbol="x"
                            return (Point(k,j,simbol))  
        for col in range(0,6):
            for i in range(0,2):
                s=0
                for j in range(i,i+5):
                    s+=b[j][col]
                if s in [20,-24]:
                    for j in range(i,i+5):
                        if b[j][col]==0:
                            if s==20:
                                simbol="o"
                            else:
                                simbol="x"
                            return (Point(k,j,simbol)) 
        '''prima diagonala '''  
        s=b[1][0]+b[2][1]+b[3][2]+b[4][3]+b[5][4]
        list=[b[1][0], b[2][1], b[3][2], b[4][3], b[5][4]]  
              
        index=list.index(0)
        if s in [20,-24]:
            if s==20:
                simbol="o"
            else:
                simbol="x"
            list2=[Point(1,0,simbol), Point(2,1,simbol), Point(3,2,simbol), Point(4,3,simbol), Point(5,4,simbol)]
            return list2[index]
            
            
        s=b[0][0]+b[1][1]+b[2][2]+b[3][3]+b[4][4]
        list=[b[0][0],b[1][1],b[2][2],b[3][3],b[4][4]]
        index=list.index(0)
        if s in [20,-24]:
            if s==20:
                simbol="o"
            else:
                simbol="x"
            list2=[Point(0,0,simbol), Point(1,1,simbol), Point(2,2,simbol), Point(3,3,simbol), Point(4,4,simbol)]
            return list2[index]
            
        
        s=b[1][1]+b[2][2]+b[3][3]+b[4][4]+b[5][5]
        list=[b[1][1], b[2][2], b[3][3], b[4][4], b[5][5]]
        index=list.index(0)
        if s in [20,-24]:
            if s==20:
                simbol="o"
            else:
                simbol="x"
            list2=[Point(1,1,simbol), Point(2,2,simbol), Point(3,3,simbol), Point(4,4,simbol), Point(5,5,simbol)]
            return list2[index]
        
        
        
        s=b[0][1]+b[1][2]+b[2][3]+b[3][4]+b[4][5]
        list=[b[0][1], b[1][2], b[2][3], b[3][4], b[4][5]]
        index=list.index(0)
        if s in [20,-24]:
            if s==20:
                simbol="o"
            else:
                simbol="x"
            list2=[Point(0,1,simbol), Point(1,2,simbol), Point(2,3,simbol), Point(3,4,simbol), Point(4,5,simbol)]
            return list2[index]
        
        
        
        ''' a doua diagonala'''
        s=b[0][4]+b[1][3]+b[2][2]+b[3][1]+b[4][0]
        list=[b[0][4], b[1][3], b[2][2], b[3][1], b[4][0]]
        index=list.index(0)
        if s in [20,-24]:
            if s==20:
                simbol="o"
            else:
                simbol="x"
            list2=[Point(0,4,simbol), Point(1,3,simbol), Point(2,2,simbol), Point(3,1,simbol), Point(4,0,simbol)]
            return list2[index]
        
       
       
        s=b[0][5]+b[1][4]+b[2][3]+b[3][2]+b[4][1]
        list=[b[0][5], b[1][4], b[2][3], b[3][2], b[4][1]]
        index=list.index(0)
        if s in [20,-24]:
            if s==20:
                simbol="o"
            else:
                simbol="x"
            list2=[Point(0,5,simbol), Point(1,4,simbol), Point(2,3,simbol), Point(3,2,simbol), Point(4,1,simbol)]
            return list2[index]
        
        
        s=b[1][4]+b[2][3]+b[3][2]+b[4][1]+b[5][0]
        list=[b[1][4], b[2][3], b[3][2], b[4][1], [5][0]]
        if s in [20,-24]:
            if s==20:
                simbol="o"
            else:
                simbol="x"
            list2=[Point(1,4,simbol), Point(2,3,simbol), Point(3,2,simbol), Point(4,1,simbol), Point(5,0,simbol)]
            return list2[index]
        
        
        s=b[1][5]+b[2][4]+b[3][3]+b[4][2]+b[5][1]
        list=[b[1][5], b[2][4], b[3][3], b[4][2], b[5][1]]
        if s in [20,-24]:
            if s==20:
                simbol="o"
            else:
                simbol="x"
            list2=[Point(1,5,simbol), Point(2,4,simbol), Point(3,3,simbol), Point(4,2,simbol), Point(5,1,simbol)]
            return list2[index]
        return None
    def fullboard(self):
        c=0
        b=self._board
        for i in range(0,6):
            for j in range(0,6):
                if b[i][j]==0:
                    c+=1
        if c==0:
            return True
        return False   
    def reia(self):
        f=open("game.txt","r")
        line=f.readline().strip()
        i=0
        while line!='':
            linie=line.split(" ")
            j=0
            for obj in linie:
                if obj=="0":
                    self._board[i][j]=0
                elif obj=="5":
                    self._board[i][j]=5
                elif obj=="-6":
                    self._board[i][j]=-6
                j+=1
            i+=1
            line=f.readline().strip()               
        print(str(self._board))
        f.close()
    def save(self):
        f=open("game.txt","w")
        b=self._board
        for i in range(0,6):
            for j in range(0,6):
                f.write(str(b[i][j]))
                f.write(" ")
            f.write("\n")
        
        f.close()
class UserInterface():
    def __init__(self,board):
        self.__board=board
        self.__start()
    def read(self):
        ok=False
        while ok==False:     
            ok=True
            x=int(input("Give x: "))
            y=int(input("Give y: "))
            x=x-1
            y=y-1
            simbol=input("Give simbol: ")
            point=Point(x,y,simbol)
            if self.__board.validare(point)==False:
                print("Invalid position!")
                ok=False            
            elif simbol!='x' and simbol!="o":
                ok=False
                print("Invalid simbol!")
            else:
                return point
    
    def __start(self): 
        print(self.__board.show().draw())
        okk=False
        while True and self.__board.fullboard()==False:   
            comanda=input("Save or play or continue the last game") 
            if comanda=="save":
                self.__board.save()            
            else:   
                if comanda=="continue":
                    self.__board.reia()   
                    print(self.__board.show().draw())        
                point=self.read()
                self.__board.makemove(point)  
                if self.__board.isGameWon()==True:
                    print(self.__board.show().draw()) 
                    okk=True  
                    print("You won!")
                    break
                self.__board.makemoveAi()
                print(self.__board.show().draw())
                if self.__board.isGameWon()==True:                
                    print("You won!") 
                    okk=True
                    break
        if okk==False:
            print("You lost! Ai wins!")           
board=Board()
ui=UserInterface(board)
print(board.show().draw())
 