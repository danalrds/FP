from random import randint
from tkinter import *
import time
import sys

class Point():
    def __init__(self,x,y):
        self._x=x 
        self._y=y
    def getX(self):
        return int(self._x)
    def getY(self):
        return int(self._y)
    
class Board():
    def __init__(self):
        self._board=[[-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1]]
    def validare(self,point):
        if point.getX()>=0 and point.getX()<=5 and point.getY()>=0 and point.getY()<=6:
            return True
        return False       
    def valid(self,point):
        if point.getX()>=0 and point.getX()<=5 and point.getY()>=0 and point.getY()<=6:
            if self._board[point.getX()][point.getY()]==-1:
                return True
        return False            
    def makeMove(self,point,user):
        if user=="player":
            u=4                      
        else:
            u=0
          
        if point.getX()>=0 and point.getX()<=5 and point.getY()>=0 and point.getY()<=6:
            if self._board[point.getX()][point.getY()]==-1:
                self._board[point.getX()][point.getY()]=u
            else:
                raise Exception("Square already taken!")
        else:
            raise Exception("Move outside the board!")    
    
    def possibleWin(self,user,lin,col):
        b=self._board         
        if user=="player":
            suma=11           
        else:
            suma=-1            
        for k in range(0,6):
            for i in range(0,4):
                s=0
                for j in range(i,i+4):
                    s+=b[k][j]
                if s==suma: 
                    for j in range(i,i+4):
                        if b[k][j]==-1:
                            p=self.findpoint(j)
                            if p.getX()==k:
                                return p 
        for col in range(0,7):
            for i in range(0,3):
                s=0
                for j in range(i,i+4):
                    s+=b[j][col]
                if s ==suma:
                    if self.valid(Point(i,col)):
                        next=Point(i,col)
                        return next
        ok=self.este_prima2(lin,col,suma,"yes")
        if ok!=None:            
            return ok       
        ok=self.este_adoua2(lin,col,suma,"yes")
        if ok!=None:            
            return ok    
        return None
    def avMoves(self):
        b=self._board
        moves=[]
        for y in range(0,7):
            for i in range(5,-1,-1):
                if b[i][y]==-1:
                    moves.append(Point(i,y))
                    break   
        #print(len(moves))                          
        return moves
    def isDraw(self):
        if self.avMoves()==[]:
            return True
        return False
    def findpoint(self,col):
        b=self._board
        for i in range(5,-1,-1):
            if b[i][col]==-1:
                return Point(i,col)
        return None      
    def encode(self,nr):
        if nr==-1:
            return '_'
        if nr==0:
            return '@'
        if nr==4:
            return '*'
    def __str__(self):
        result=""
        for line in self._board:
            result+=self.encode(line[0])+"|"+self.encode(line[1])+"|"+self.encode(line[2])+"|"+self.encode(line[3])+"|"+self.encode(line[4])+"|"+self.encode(line[5])+"|"+self.encode(line[6])+"\n"
        return result
            
    def isGameWon(self,lp,cp,la,ca):
        b=self._board
        for k in range(0,6):
            for i in range(0,4):
                s=0
                for j in range(i,i+4):
                    s+=b[k][j]
                if s in [0,16]:
                    return True
        for col in range(0,7):
            for i in range(0,3):
                s=0
                for j in range(i,i+4):
                    s+=b[j][col]
                if s in [0,16]:
                    return True        
                
        ok=self.este_prima2(lp,cp,16,"no")
        if ok==True:
            return True        
        ok=self.este_prima2(la, ca,0,"no")
        if ok==True:
            return True  
        ok=self.este_adoua2(lp,cp,16,"no")
        if ok==True:
            return True        
        ok=self.este_adoua2(la, ca,0,"no")
        if ok==True:
            return True              
        return False
    def este_prima2(self,linie,coloana,suma,ms):
        b=self._board
        list=[]       
        s=linie+coloana
        if s>=5:
            linie=5
        else:
            linie=s
        coloana=s-linie        
        while True:            
            if self.validare(Point(linie,coloana))==True:
                el=(linie,coloana)
                list.append(el)
            else:
                break
            linie=linie-1
            coloana+=1
        n=len(list)
        
        for i in range(0,n-3):
            s=0
            for j in range(i,i+4):
                s+=b[list[j][0]][list[j][1]]
            if s==suma:
                if ms=="yes":
                    for j in range(i,i+4):
                        if b[list[j][0]][list[j][1]] ==-1:
                            linia=list[j][0]
                            coloana=list[j][1]
                            if self.findpoint(coloana)==Point(linia,coloana):
                                return Point(list[j][0],list[j][1]) 
                    return None 
                else:
                    return True      
                
        return None
    def este_adoua2(self,lin,col,suma,ms):
        b=self._board
        list=[]       
        if lin<col:
            linie=0
            coloana=col-lin
        else:
            linie=lin-col
            coloana=0      
        while True:            
            if self.validare(Point(linie,coloana))==True:
                el=(linie,coloana)
                list.append(el)
            else:
                break
            linie+=1
            coloana+=1
        n=len(list)
        
        for i in range(0,n-3):
            s=0
            for j in range(i,i+4):
                s+=b[list[j][0]][list[j][1]]
            if s==suma:
                if ms=="yes":
                    for j in range(i,i+4):
                        if b[list[j][0]][list[j][1]] ==-1:
                            linia=list[j][0]
                            coloana=list[j][1]
                            if self.findpoint(coloana)==Point(linia,coloana):
                                return Point(list[j][0],list[j][1]) 
                    return None 
                else:
                    return True 
                
        return None
    
    
class Game():
    def __init__(self,board):
        self.__board=board
    def makeMoveAI(self,lp,cp,la,ca):
        next=self.__board.possibleWin("ai",la,ca)
        if next!=None:            
            self.__board.makeMove(next,"ai")            
            return next           
        else:
            contra=self.__board.possibleWin("player",lp,cp)
            if contra!=None:
                self.__board.makeMove(contra,"ai")   
                return contra             
            else:
                availableMoves=self.__board.avMoves()
                randMove=randint(0,len(availableMoves)-1)
                self.__board.makeMove(availableMoves[randMove],"ai")   
                return availableMoves[randMove]             
    def makeMovePlayer(self,point):
        self.__board.makeMove(point,"player")        
    def getBoard(self):
        return self.__board

class UserInterface():
    def __init__(self,game,parent):
        self.__game=game        
        self.__start()
    def __start(self):
        crtPlayer=4
        lp=0
        la=0
        cp=0
        ca=0
        while self.__game.getBoard().isGameWon(lp,cp,la,ca)==False and self.__game.getBoard().isDraw()==False:
            
            if crtPlayer==4:
                print(self.__game.getBoard()) 
                y=int(input("Y coord: "))
                point=self.__game.getBoard().findpoint(y)
                try:
                    self.__game.makeMovePlayer(point)  
                    lp=point.getX()
                    cp=point.getY()                                    
                    crtPlayer=0
                except Exception as exc:
                    print(exc)
            else:
                point=self.__game.makeMoveAI(lp,cp,la,ca)
                la=point.getX()
                ca=point.getY() 
                crtPlayer=4
        print(self.__game.getBoard())
        if self.__game.getBoard().isGameWon(lp,cp,la,ca)==True:
            if crtPlayer==4:
                print("Computer has won.")
            elif crtPlayer==0:
                print("Human has won.")
        else:
            if self.__game.getBoard().isDraw()==True:
                print("It is a draw.")


root = Tk()
root.resizable(width=FALSE, height=FALSE)
root.geometry("728x624")
root.configure(bg="white", cursor="@assets/cursor_blue.cur")
root.title("Connect Four")
GameBoard=Board()
game=Game(GameBoard)
ui=UserInterface(game,root)