from pip._vendor.requests.packages.urllib3.packages.six import moves
class Point:
    def __init__(self,x,y):
        self._x=x
        self._y=y
    def getx(self):
        return self._x
    def gety(self):
        return self._y
class Board:
    def __init__(self):
        self._board=[[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
    def makeMove(self,point,user):
        o=0
        if user=="player":
            o=3
        else:
            o=0
        if point.getx()>-1 and point.getx()<3 and point.gety()>-1 and point.gety()<3:
            if self._board[point.getx(),point.gety()]==-1:
                self._board[point.getx(),point.gety()]=o
            else:
                raise Exception("Position already taken!")
        else:
            raise Exception("Move outside the board!")
    
    def isgamewon(self):
        for l in self._board:
            if sum(l) in [0,9]:
                return True
        for i in range(0,3):
            sum= l[0,i]+l[1,i]+l[2,i] 
            if sum in  [0,9]:
                return True
        l=self._board
        sum=l[0,0]+l[1,1]+l[2,2]
        if sum in  [0,9]:
                return True
        sum=l[1,3]+l[2,2]+l[3,1]
        if sum in  [0,9]:
                return True   
        return False
    
    def avmoves(self):
        moves=[]
        b=self._board
        for l in range(0,3):
            for c in range(0,3):
                if b[l][c]==-1:
                    moves.append(Point(l,c))
        return moves
    
    def isdraw(self):
        if self.avmoves()==[]:
            return True
        return False
    def encode(self,number):
        if number==-1:
            return " "
        if number==0:
            return "0"
        if number==3:
            return "x"
     
    def __str__(self):
        b=""
        result=""
        ln=0        
        for line in self._board:
            result+=self.encode(line[0])+"/"+self.encode(line[1])+"/"+self.encode(line[2])
            if ln in [0,1]:
                   b+="______\n"
                   ln+=1
class Game:
    def __init__(self,board):
        self._board=board
    def makeMoveUi(self):
        availablemoves=self._board.avmoves()
        randmove=random(0,len(availablemoves)-1)
        self._board.makeMove(availablemoves)              
    def makeMovePlayer(self,point):
        self._board.makeMove(point,"player")
class UserInterface:
    def __init__(self,game):
        self._game=game
        self._start()
    def start(self):
        while self._game.getBoard().isgamewon()==False:
            print("")
        
gameboard=Board()

